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
from google.adk.planners import PlanReActPlanner
from google.adk.tools.agent_tool import AgentTool

from smallbizpal.agents.marketing_generator.config import (
    MARKETING_GENERATOR_CONFIG,
)

from .sub_agents import content_creation_agent
from .tools import retrieve_business_profile

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
)

# root_agent = marketing_generator_agent
