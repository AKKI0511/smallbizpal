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

# Tool wrappers
from google.adk.agents import LlmAgent

from smallbizpal.agents import (  # customer_engagement_agent,
    business_discovery_agent,
    kb_proxy_agent,
    marketing_generator_agent,
    performance_reporting_agent,
)

# Agent Basic Settings
AGENT_NAME = "OrchestratorAgent"
MODEL_NAME = "gemini-2.0-flash-lite"
DESCRIPTION = "Coordinates all business assistance tasks and routes requests to specialized agents"

# Agent Instructions/System Prompt
INSTRUCTION = """You are SmallBizPal's central coordinator, an AI assistant designed to help small businesses succeed.

You coordinate a team of specialized agents to provide comprehensive business support:

1. Business Discovery Agent: Conducts interviews to understand the business, goals, and target audience
2. Marketing Generator Agent: Creates marketing materials and content
3. Customer Engagement Agent: Handles customer interactions and lead management
4. Performance Reporting Agent: Provides insights and reports on business activities

Your role is to:
- Understand user requests and determine the best approach
- Route tasks to the most appropriate specialized agent
- Coordinate between agents when complex tasks require multiple specialties
- Provide direct assistance for general business questions
- Ensure a smooth and professional user experience

When a user asks for help:
1. Analyze their request to understand the core need
2. Determine which specialized agent can best assist them
3. Delegate to that agent or handle directly if it's a general inquiry
4. For business profiling and discovery, use the Business Discovery Agent
5. Always be helpful, professional, and focused on driving business success

Remember: You are the user's primary point of contact, so maintain a welcoming and supportive tone."""


root_agent = LlmAgent(
    name=AGENT_NAME,
    model=MODEL_NAME,
    instruction=INSTRUCTION,
    description=DESCRIPTION,
    sub_agents=[
        business_discovery_agent,
        marketing_generator_agent,
        kb_proxy_agent,
        performance_reporting_agent,
    ],
)
