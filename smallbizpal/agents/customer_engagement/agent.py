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

from smallbizpal.agents.customer_engagement.config import (
    CUSTOMER_ENGAGEMENT_CONFIG,
)

from .tools import (
    ask_internal_kb,
    schedule_meeting,
)

customer_engagement_agent = LlmAgent(
    name=CUSTOMER_ENGAGEMENT_CONFIG["name"],
    model=CUSTOMER_ENGAGEMENT_CONFIG["model"],
    instruction=CUSTOMER_ENGAGEMENT_CONFIG["instruction"],
    description=CUSTOMER_ENGAGEMENT_CONFIG["description"],
    tools=[
        ask_internal_kb,
        schedule_meeting,
    ],
)

# root_agent = customer_engagement_agent
