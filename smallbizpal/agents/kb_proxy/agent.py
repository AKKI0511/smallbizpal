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

from smallbizpal.agents.kb_proxy.config import (
    KB_PROXY_CONFIG,
)

from .tools import search_private_kb

kb_proxy_agent = LlmAgent(
    name=KB_PROXY_CONFIG["name"],
    model=KB_PROXY_CONFIG["model"],
    instruction=KB_PROXY_CONFIG["instruction"],
    description=KB_PROXY_CONFIG["description"],
    tools=[search_private_kb],
)

# root_agent = kb_proxy_agent
