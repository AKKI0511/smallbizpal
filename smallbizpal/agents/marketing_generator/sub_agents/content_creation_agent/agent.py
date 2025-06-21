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

from google.adk.agents import LlmAgent

from smallbizpal.agents.marketing_generator.config import CONTENT_CREATION_AGENT_CONFIG

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
    disallow_transfer_to_parent=CONTENT_CREATION_AGENT_CONFIG[
        "disallow_transfer_to_parent"
    ],
    disallow_transfer_to_peers=CONTENT_CREATION_AGENT_CONFIG[
        "disallow_transfer_to_peers"
    ],
)
