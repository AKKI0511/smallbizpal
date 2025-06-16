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
from .tools import (
    ask_user_input,
    get_all_business_data,
    get_business_profile_status,
    search_business_data,
    store_business_data,
)

# Build tools list based on config
tools = []

# Input tools
if TOOLS_CONFIG.get("ask_user_input", {}).get("enabled", False):
    tools.append(ask_user_input)

# Storage tools - simple and flexible
if TOOLS_CONFIG.get("store_business_data", {}).get("enabled", True):
    tools.extend(
        [
            store_business_data,  # type: ignore
            get_business_profile_status,  # type: ignore
            get_all_business_data,  # type: ignore
            search_business_data,  # type: ignore
        ]
    )

business_discovery_agent = LlmAgent(
    name=AGENT_NAME,
    model=MODEL_NAME,
    instruction=INSTRUCTION,
    description=DESCRIPTION,
    tools=tools,
)

# root_agent = business_discovery_agent
