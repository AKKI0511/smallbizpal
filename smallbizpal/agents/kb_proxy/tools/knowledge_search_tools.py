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

from google.adk.tools import ToolContext

from smallbizpal.shared.services import knowledge_base_service


def search_private_kb(query: str, tool_context: ToolContext) -> str:
    """
    Searches the private knowledge base for information relevant to the query.

    For MVP, this simply returns the entire business profile data.
    Later this will be upgraded to vector search with RAG.

    Args:
        query: The search query from the customer engagement agent
        tool_context: The context of the tool.

    Returns:
        Complete business profile data from the knowledge base
    """
    try:
        user_id = tool_context._invocation_context.session.user_id

        # Get business profile from knowledge base service
        business_profile = knowledge_base_service.get_business_profile(user_id)

        if not business_profile:
            return "No business information available. Please complete the business profile setup."

        # Get all business data
        business_data = business_profile.get_all_data()

        if not business_data:
            return "No business information available. Please complete the business profile setup."

        # For MVP: Simply return the entire business profile as JSON string
        return json.dumps(business_data, indent=2)

    except Exception as e:
        return f"Error accessing knowledge base: {str(e)}"
