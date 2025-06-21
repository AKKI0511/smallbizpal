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

import json
from datetime import datetime
from pathlib import Path

from google.adk.tools import ToolContext


def schedule_meeting(
    name: str, email: str, topic: str, tool_context: ToolContext, preferred_time: str = ""
) -> str:
    """
    Schedules a meeting with the business owner for a potential customer.

    Args:
        name: The name of the potential customer.
        email: The email address of the potential customer.
        topic: The topic or reason for the meeting.
        tool_context: The context of the tool.
        preferred_time: Optional preferred time for the meeting.

    Returns:
        A confirmation message to be shown to the user.
    """
    try:
        user_id = tool_context._invocation_context.session.user_id
        
        # Create user-specific leads directory if it doesn't exist
        leads_dir = Path("data") / user_id / "leads"
        leads_dir.mkdir(parents=True, exist_ok=True)

        # Create lead record
        lead_data = {
            "name": name,
            "email": email,
            "topic": topic,
            "preferred_time": preferred_time,
            "timestamp": datetime.now().isoformat(),
            "status": "new",
            "source": "customer_engagement_agent",
        }

        # Save to user-specific leads file
        leads_file = leads_dir / "leads.json"
        leads = []

        if leads_file.exists():
            try:
                with open(leads_file, "r") as f:
                    leads = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                leads = []

        leads.append(lead_data)

        with open(leads_file, "w") as f:
            json.dump(leads, f, indent=2)

        # Also store in customer interactions for the knowledge base
        try:
            from smallbizpal.shared.services import knowledge_base_service

            interaction_data = {
                "type": "meeting_request",
                "customer_name": name,
                "customer_email": email,
                "topic": topic,
                "preferred_time": preferred_time,
                "timestamp": datetime.now().isoformat(),
                "status": "scheduled",
            }
            knowledge_base_service.store_customer_interaction(user_id, interaction_data)
        except Exception:
            pass  # Don't fail if KB service is unavailable

        return f"""Thank you, {name}! I've successfully scheduled a meeting request for you.

📅 **Meeting Details:**
- **Name:** {name}
- **Email:** {email}
- **Topic:** {topic}
- **Preferred Time:** {preferred_time if preferred_time else "To be determined"}

Our team will contact you at {email} within 24 hours to confirm the meeting time and provide further details.

Is there anything else I can help you with while we're here?"""

    except Exception as e:
        return f"""I apologize, but there was an issue scheduling your meeting. Please try again or contact us directly.

You can reach us at:
- Email: [Business will provide contact email]
- Phone: [Business will provide contact phone]

Error details: {str(e)}"""
