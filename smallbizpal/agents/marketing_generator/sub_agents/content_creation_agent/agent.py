#   Copyright 2025 Akshat Deepak Joshi
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from typing import Optional

from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types

from smallbizpal.agents.marketing_generator.config import CONTENT_CREATION_AGENT_CONFIG
from smallbizpal.agents.marketing_generator.tools import save_content_to_kb


def content_storage_callback(
    callback_context: CallbackContext, **kwargs
) -> Optional[types.Content]:
    """
    After-agent callback that stores the created content in the knowledge base.
    The structured output will still be returned to the parent agent as-is.
    """
    try:
        # Get the agent's output from the output_key
        # When using output_schema, ADK stores the parsed object, not JSON string
        agent_output = callback_context.state.get("content_created")

        if not agent_output:
            print("No content found in output_key 'content_created'")
            return None

        # The output is already parsed by ADK when using output_schema
        if isinstance(agent_output, dict):
            content_data = agent_output
        elif hasattr(agent_output, "model_dump"):
            # If it's a Pydantic model instance
            content_data = agent_output.model_dump()
        else:
            print(f"Unexpected agent_output type: {type(agent_output)}")
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

        # Store the content in the knowledge base
        storage_result = save_content_to_kb(
            platform=platform, content=content, asset_type=asset_type
        )

        print(f"Content stored successfully: {storage_result}")

        # Return None to let the original structured output go through
        # The parent agent will receive the structured JSON response
        return None

    except Exception as e:
        print(f"Error in content_storage_callback: {e}")
        # Return None to allow the original response to go through
        return None


# This agent is designed to be used as a "tool" by its parent.
# It receives a structured Pydantic model as input and uses callbacks
# to store the generated content while returning it to the parent agent.
content_creation_agent = LlmAgent(
    name=CONTENT_CREATION_AGENT_CONFIG["name"],
    model=CONTENT_CREATION_AGENT_CONFIG["model"],
    description=CONTENT_CREATION_AGENT_CONFIG["description"],
    instruction=CONTENT_CREATION_AGENT_CONFIG["instruction"],
    input_schema=CONTENT_CREATION_AGENT_CONFIG["input_schema"],
    output_schema=CONTENT_CREATION_AGENT_CONFIG["output_schema"],
    output_key=CONTENT_CREATION_AGENT_CONFIG["output_key"],
    after_agent_callback=content_storage_callback,
)
