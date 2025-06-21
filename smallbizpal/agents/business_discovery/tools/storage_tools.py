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

from typing import Any, Dict, List

from google.adk.tools import ToolContext


def store_business_data(data: Dict[str, Any], tool_context: ToolContext) -> str:
    """Store any business information in the knowledge base.

    This tool accepts any dictionary of business information and stores it.
    No specific schema is required - just provide key-value pairs of business data.

    Args:
        data: Dictionary containing any business information (e.g., {"company_name": "ABC Corp", "industry": "tech"})
        tool_context: The context of the tool.

    Returns:
        Confirmation message with storage results
    """
    from smallbizpal.shared.services.knowledge_base import knowledge_base_service

    user_id = tool_context._invocation_context.session.user_id
    try:
        result = knowledge_base_service.update_business_profile(user_id, data)

        if result["status"] == "success":
            return (
                f"✅ Successfully stored business information!\n"
                f"Added fields: {', '.join(result['updated_fields'])}\n"
                f"Total fields in profile: {result['total_fields']}\n"
                f"Profile updates: {result['total_updates']}"
            )
        else:
            return f"❌ {result['message']}"

    except Exception as e:
        return f"❌ Error storing business data: {str(e)}"


def get_business_profile_status(tool_context: ToolContext) -> str:
    """Get current business profile status and summary.

    Args:
        tool_context: The context of the tool.

    Returns:
        Summary of what business information has been collected so far
    """
    from smallbizpal.shared.services.knowledge_base import knowledge_base_service

    user_id = tool_context._invocation_context.session.user_id
    try:
        summary = knowledge_base_service.get_profile_summary(user_id)

        if summary["profile_exists"]:
            return (
                f"📊 Business Profile Status:\n"
                f"Total fields stored: {summary['total_fields']}\n"
                f"Last updated: {summary['updated_at']}\n"
                f"Total updates: {summary['total_updates']}\n"
                f"Sample fields: {', '.join(summary['sample_fields'])}"
            )
        else:
            return "📄 No business profile exists yet. Start collecting business information!"

    except Exception as e:
        return f"❌ Error getting profile status: {str(e)}"


def get_all_business_data(tool_context: ToolContext) -> str:
    """Get all stored business data.

    Args:
        tool_context: The context of the tool.

    Returns:
        All business information that has been collected
    """
    from smallbizpal.shared.services.knowledge_base import knowledge_base_service

    user_id = tool_context._invocation_context.session.user_id
    try:
        data = knowledge_base_service.get_business_data(user_id)

        if data:
            output = "📋 All Business Data:\n"
            for key, value in data.items():
                output += f"• {key}: {value}\n"
            return output
        else:
            return "📄 No business data stored yet."

    except Exception as e:
        return f"❌ Error retrieving business data: {str(e)}"


def search_business_data(search_terms: List[str], tool_context: ToolContext) -> str:
    """Search for specific business information.

    Args:
        search_terms: List of terms to search for in the business data
        tool_context: The context of the tool.

    Returns:
        Matching business information
    """
    from smallbizpal.shared.services.knowledge_base import knowledge_base_service

    user_id = tool_context._invocation_context.session.user_id
    try:
        results = knowledge_base_service.search_business_data(user_id, search_terms)

        if results:
            output = f"🔍 Search results for: {', '.join(search_terms)}\n"
            for key, value in results.items():
                output += f"• {key}: {value}\n"
            return output
        else:
            return f"🔍 No results found for: {', '.join(search_terms)}"

    except Exception as e:
        return f"❌ Error searching business data: {str(e)}"
