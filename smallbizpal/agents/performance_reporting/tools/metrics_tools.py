#   Copyright 2025 Akshat Deepak Joshi

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from collections import Counter
from datetime import UTC, date, datetime
from typing import Any, Dict, Optional

from google.adk.tools import ToolContext

from smallbizpal.shared.services import knowledge_base_service


def date_from_iso(timestamp_str: str) -> Optional[date]:
    """Convert ISO timestamp string to date object.

    Args:
        timestamp_str: ISO format timestamp string

    Returns:
        date object or None if parsing fails
    """
    try:
        # Handle various timestamp formats
        if "T" in timestamp_str:
            # ISO format with time
            dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
        else:
            # Date only format
            dt = datetime.fromisoformat(timestamp_str)
        return dt.date()
    except (ValueError, AttributeError):
        return None


def collect_metrics(  # noqa: C901
    tool_context: ToolContext, run_date: Optional[str] = None  # noqa: C901
) -> Dict[str, Any]:  # noqa: C901
    """Collect performance metrics from the knowledge base for a specific date.

    Args:
        tool_context: The context of the tool.
        run_date: Date to collect metrics for (YYYY-MM-DD format).
                 Defaults to today if not provided.

    Returns:
        Dictionary containing collected metrics data
    """
    try:
        user_id = tool_context._invocation_context.session.user_id

        # Parse target date
        if run_date:
            try:
                target_date = datetime.strptime(run_date, "%Y-%m-%d").date()
            except ValueError:
                return {
                    "error": f"Invalid date format: {run_date}. Use YYYY-MM-DD format.",
                    "success": False,
                }
        else:
            target_date = datetime.now(UTC).date()

        # Initialize metrics
        metrics = {
            "date": target_date.strftime("%Y-%m-%d"),
            "leads_count": 0,
            "leads_details": [],
            "interactions_count": 0,
            "top_questions": [],
            "marketing_assets_count": 0,
            "marketing_assets": [],
            "success": True,
        }

        # Collect customer interactions
        interactions = knowledge_base_service.get_customer_interactions(user_id)

        # Filter interactions by date and categorize
        daily_interactions = []
        daily_leads = []
        questions = []

        for interaction in interactions:
            interaction_date = date_from_iso(interaction.get("timestamp", ""))
            if interaction_date == target_date:
                daily_interactions.append(interaction)

                # Check if it's a lead (meeting request)
                if interaction.get("type") == "meeting_request":
                    lead_data = {
                        "name": interaction.get("customer_name", "Unknown"),
                        "email": interaction.get("customer_email", ""),
                        "topic": interaction.get("topic", ""),
                        "preferred_time": interaction.get("preferred_time", ""),
                        "timestamp": interaction.get("timestamp", ""),
                    }
                    daily_leads.append(lead_data)

                # Extract questions for analysis
                if interaction.get("type") in ["question", "inquiry"]:
                    question_text = interaction.get(
                        "question", interaction.get("topic", "")
                    )
                    if question_text:
                        questions.append(question_text)

        # Also check user-specific leads.json file for additional lead data
        try:
            import json
            from pathlib import Path

            leads_file = Path("data") / user_id / "leads" / "leads.json"
            if leads_file.exists():
                with open(leads_file, "r") as f:
                    leads_data = json.load(f)

                for lead in leads_data:
                    lead_date = date_from_iso(lead.get("timestamp", ""))
                    if lead_date == target_date:
                        # Avoid duplicates by checking if already in daily_leads
                        if not any(
                            l.get("email") == lead.get("email")
                            for l in daily_leads  # noqa: E741
                        ):
                            lead_data = {
                                "name": lead.get("name", "Unknown"),
                                "email": lead.get("email", ""),
                                "topic": lead.get("topic", ""),
                                "preferred_time": lead.get("preferred_time", ""),
                                "timestamp": lead.get("timestamp", ""),
                            }
                            daily_leads.append(lead_data)
        except Exception:
            pass  # Continue without leads.json data if there's an issue

        # Collect marketing assets
        marketing_assets = knowledge_base_service.get_marketing_assets(user_id)
        daily_assets = []

        for asset in marketing_assets:
            asset_date = date_from_iso(str(asset.get("created_at", "")))
            if asset_date == target_date:
                asset_data = {
                    "id": asset.get("id", ""),
                    "content_type": asset.get(
                        "content_type", asset.get("asset_type", "Unknown")
                    ),
                    "platform": asset.get("platform", "Universal"),
                    "content": (
                        asset.get("content", "")[:100] + "..."
                        if len(asset.get("content", "")) > 100
                        else asset.get("content", "")
                    ),
                    "created_at": asset.get("created_at", ""),
                }
                daily_assets.append(asset_data)

        # Analyze top questions
        if questions:
            question_counts = Counter(questions)
            top_questions = [
                {"question": q, "frequency": count}
                for q, count in question_counts.most_common(5)
            ]
        else:
            top_questions = []

        # Update metrics
        metrics.update(
            {
                "leads_count": len(daily_leads),
                "leads_details": daily_leads,
                "interactions_count": len(daily_interactions),
                "top_questions": top_questions,
                "marketing_assets_count": len(daily_assets),
                "marketing_assets": daily_assets,
            }
        )

        return metrics

    except Exception as e:
        return {
            "error": f"Failed to collect metrics: {str(e)}",
            "success": False,
            "date": run_date or datetime.now(UTC).date().strftime("%Y-%m-%d"),
        }
