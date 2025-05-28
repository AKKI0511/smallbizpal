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


# Orchestrator Agent Configuration

# Agent Basic Settings
AGENT_NAME = "OrchestratorAgent"
MODEL_NAME = "gemini-1.5-flash"
DESCRIPTION = "Coordinates all business assistance tasks and routes requests to specialized agents"

# Agent Instructions/System Prompt
INSTRUCTION = """You are SmallBizPal's central coordinator, an AI assistant designed to help small businesses succeed.

You coordinate a team of specialized agents to provide comprehensive business support:

1. Business Discovery Agent: Conducts interviews to understand the business, goals, and target audience
2. Marketing Generator Agent: Creates marketing materials and content (coming soon)
3. Customer Engagement Agent: Handles customer interactions and lead management (coming soon)
4. Performance Reporting Agent: Provides insights and reports on business activities (coming soon)

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

# Agent Behavior Settings
BEHAVIOR_CONFIG = {
    "conversational_style": "professional_friendly",
    "response_length": "medium",
    "proactive": True,
    "follow_up_enabled": True,
    "delegation_enabled": True,
    "coordination_mode": "intelligent_routing",
}

# Task Configuration
TASK_CONFIG = {
    "max_iterations": 15,
    "timeout": 600,  # 10 minutes for complex coordination tasks
    "retry_attempts": 3,
    "auto_delegate": True,
    "confirmation_required": False,
}

# Tools Configuration (orchestrator typically doesn't need many tools)
TOOLS_CONFIG = {
    # Orchestrator mainly delegates to sub-agents
    # Add tools here if needed for coordination tasks
}

# Delegation Rules
DELEGATION_CONFIG = {
    "business_discovery": {
        "keywords": [
            "business",
            "profile",
            "interview",
            "discovery",
            "about your business",
            "tell me about",
        ],
        "agent": "BusinessDiscoveryAgent",
        "auto_delegate": True,
    },
    "marketing": {
        "keywords": [
            "marketing",
            "content",
            "social media",
            "advertising",
            "promotion",
        ],
        "agent": "MarketingGeneratorAgent",
        "auto_delegate": False,  # Not implemented yet
        "fallback_message": "Marketing assistance is coming soon! For now, I can help you with business discovery.",
    },
    "customer_engagement": {
        "keywords": ["customer", "lead", "engagement", "communication", "follow-up"],
        "agent": "CustomerEngagementAgent",
        "auto_delegate": False,  # Not implemented yet
        "fallback_message": "Customer engagement features are coming soon! For now, I can help you with business discovery.",
    },
    "reporting": {
        "keywords": ["report", "analytics", "performance", "metrics", "insights"],
        "agent": "PerformanceReportingAgent",
        "auto_delegate": False,  # Not implemented yet
        "fallback_message": "Performance reporting is coming soon! For now, I can help you with business discovery.",
    },
}

# Prompts for coordination
PROMPTS = {
    "welcome": "Hello! I'm SmallBizPal, your AI-powered small business assistant. \
          I'm here to help you succeed with business discovery, marketing, customer \
          engagement, and more. How can I assist you today?",
    "delegation": "I'm connecting you with our {agent_type} specialist who can better \
          assist you with this request.",
    "fallback": "I understand you're looking for help with {topic}. While that feature\
          is being developed, I can help you with business discovery and profiling. \
          Would you like to start there?",
    "error": "I apologize for the confusion. Let me try a different approach to help you.",
    "completion": "Is there anything else I can help you with today? I'm here to support\
          your business success!",
}
