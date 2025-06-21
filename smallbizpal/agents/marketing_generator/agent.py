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

from datetime import UTC, datetime
from typing import Any, Dict, Optional

from google.adk.agents import LlmAgent
from google.adk.planners import PlanReActPlanner
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.genai import types

from smallbizpal.agents.marketing_generator.config import (
    CONTENT_CREATION_AGENT_CONFIG,
    MARKETING_GENERATOR_CONFIG,
)
from smallbizpal.shared.services import knowledge_base_service

from .sub_agents import content_creation_agent
from .tools import retrieve_business_profile


def content_storage_callback(
    tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext, tool_response: Any
) -> Optional[types.Content]:
    """
    After-tool callback that stores content created by the ContentCreationAgent.
    This runs in the marketing generator agent's context with the correct user_id.
    """
    try:
        # Check if this callback is for the ContentCreationAgent tool
        tool_name = tool.name
        if tool_name != CONTENT_CREATION_AGENT_CONFIG["name"]:
            return None  # Not our tool, pass through

        # print(f"ARGE HERE: {args}")
        # print(f"TOOL RESULT HERE: {tool_response}")

        if not tool_response:
            print("No tool result found in callback context")
            return None

        # Parse the tool result - it should be the structured JSON from ContentCreationAgent
        if isinstance(tool_response, str):
            import json

            try:
                content_data = json.loads(tool_response)
            except json.JSONDecodeError:
                print(f"Failed to parse tool result as JSON: {tool_response}")
                return None
        elif isinstance(tool_response, dict):
            content_data = tool_response
        else:
            print(f"Unexpected tool result type: {type(tool_response)}")
            return None

        # Extract the required fields
        content = content_data.get("content", "")
        platform = content_data.get("platform", "")
        asset_type = content_data.get("asset_type", "")

        if not all([content, platform, asset_type]):
            print(
                f"Missing required fields: content={bool(content)}, platform={bool(platform)}, asset_type={bool(asset_type)}"
            )
            return None

        # Get user_id from the marketing generator agent's context (correct session)
        user_id = tool_context._invocation_context.session.user_id

        # Store the content using knowledge_base_service
        asset_data = {
            "platform": platform,
            "content": content,
            "asset_type": asset_type,
            "created_at": datetime.now(UTC).isoformat(),
        }

        knowledge_base_service.store_marketing_asset(user_id, asset_data)
        print(
            f"Content stored successfully for user: {user_id} - {asset_type} for {platform}"
        )

        # Return None to let the original tool result go through
        return None

    except Exception as e:
        print(f"Error in content_storage_callback: {e}")
        # Return None to allow the original response to go through
        return None


# The root MarketingGenerator agent orchestrates the entire workflow.
# It uses its own intelligence to create a plan and then delegates
# the execution of that plan to the ContentCreationAgent.
marketing_generator_agent = LlmAgent(
    name=MARKETING_GENERATOR_CONFIG["name"],
    model=MARKETING_GENERATOR_CONFIG["model"],
    description=MARKETING_GENERATOR_CONFIG["description"],
    instruction=MARKETING_GENERATOR_CONFIG["instruction"],
    tools=[retrieve_business_profile, AgentTool(content_creation_agent)],
    planner=PlanReActPlanner(),
    after_tool_callback=content_storage_callback,
)

# root_agent = marketing_generator_agent
