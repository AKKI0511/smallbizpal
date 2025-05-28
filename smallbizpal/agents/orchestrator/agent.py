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

from google.adk.agents import LlmAgent

from .config import AGENT_NAME, DESCRIPTION, INSTRUCTION, MODEL_NAME, TOOLS_CONFIG

# Build tools list based on config (orchestrator typically has few tools)
tools = []
for tool_name, tool_config in TOOLS_CONFIG.items():
    if tool_config.get("enabled", True):
        # Import and add tools as needed
        # tools.append(imported_tool)
        pass

orchestrator_agent = LlmAgent(
    name=AGENT_NAME,
    model=MODEL_NAME,
    instruction=INSTRUCTION,
    description=DESCRIPTION,
    tools=tools,
    # sub_agents will be added later from smallbizpal.agent
)
