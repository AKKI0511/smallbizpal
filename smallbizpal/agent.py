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
"""
SmallBizPal - AI-Powered Small Business Assistant

This is the main entry point for the SmallBizPal ADK multi-agent system.
According to ADK conventions, this file must contain a 'root_agent' variable.
"""

from smallbizpal.agents import (
    business_discovery_agent,
    customer_engagement_agent,
    marketing_generator_agent,
    orchestrator_agent,
)

# The orchestrator agent serves as our root agent and coordinates all other agents
root_agent = orchestrator_agent

# Configure sub-agents for the orchestrator
root_agent.sub_agents = [
    business_discovery_agent,
    marketing_generator_agent,
    customer_engagement_agent,
    # TODO: Add other agents as they are implemented
    # performance_reporting_agent
]

# Export for easy importing
__all__ = ["root_agent"]
