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

from typing import Any, Dict

from smallbizpal.shared.services import knowledge_base_service


def retrieve_business_profile() -> Dict[str, Any]:
    """Retrieve the current business profile for marketing content generation.

    Returns:
        Dictionary containing business profile data including:
        - business_name: Name of the business
        - industry: Business industry/sector
        - target_audience: Description of target customers
        - unique_value_proposition: What makes the business unique
        - brand_voice: Tone and personality for communications
        - products_services: List of products/services offered
        - business_goals: Current business objectives
        - marketing_budget: Available marketing budget
        - current_marketing_activities: Existing marketing efforts
        - social_media_presence: Current social media accounts
        - competitive_advantages: Key differentiators

    Raises:
        Exception: If no business profile is found
    """
    try:
        # Retrieve business profile from knowledge base
        business_profile = knowledge_base_service.get_business_profile()

        if not business_profile:
            return {
                "error": "No business profile found",
                "message": "Please complete business discovery first",
                "status": "missing_profile",
            }

        # Convert to dictionary for easier agent consumption
        profile_data = business_profile.get_all_data()

        # Add marketing-specific metadata
        profile_data["retrieved_at"] = profile_data.get("updated_at", "unknown")
        return profile_data

    except Exception as e:
        return {
            "error": "Failed to retrieve business profile",
            "message": str(e),
            "status": "retrieval_error",
        }
