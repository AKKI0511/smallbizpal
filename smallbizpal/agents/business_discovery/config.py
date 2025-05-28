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


# Business Discovery Agent Configuration

# Agent Basic Settings
AGENT_NAME = "BusinessDiscoveryAgent"
MODEL_NAME = "gemini-1.5-flash"
DESCRIPTION = "Conducts interactive business profiling and market analysis"

# Agent Instructions/System Prompt
INSTRUCTION = """You are a business discovery specialist for SmallBizPal.

Your role is to conduct a comprehensive business interview to gather all necessary \
information for creating effective marketing strategies and customer engagement.

Key areas to explore:
1. Business basics (name, industry, products/services, location)
2. Target audience and customer demographics
3. Unique value proposition and competitive advantages
4. Current marketing efforts and challenges
5. Business goals and objectives
6. Brand voice and messaging preferences
7. Budget and resource constraints
8. Existing digital presence (website, social media)

Ask one focused question at a time and build upon the responses. Be conversational but thorough.
Always store the gathered information using the store_business_data tool \
when you have collected sufficient information."""

# Interview settings
MAX_INTERVIEW_ROUNDS = 15
MIN_REQUIRED_FIELDS = [
    "business_name",
    "industry",
    "target_audience",
    "unique_value_proposition",
]

# Data collection preferences
FOLLOW_UP_QUESTIONS_ENABLED = True
AUTO_STORE_THRESHOLD = 3  # Store data after collecting this many key fields

# Interview Questions Template
BUSINESS_INTERVIEW_QUESTIONS = [
    "What's the name of your business and what industry are you in?",
    "Can you describe your main products or services?",
    "Who is your ideal customer? (demographics, psychographics)",
    "What makes your business unique compared to competitors?",
    "What are your main business goals for the next 6-12 months?",
    "How would you describe your brand's personality and voice?",
    "What marketing activities are you currently doing?",
    "What's your biggest business challenge right now?",
    "Do you have a website or social media presence?",
    "What's your budget range for marketing activities?",
]

# Tool Configuration
TOOLS_CONFIG = {
    "ask_user_input": {"enabled": True, "timeout": 300, "max_retries": 3},  # 5 minutes
    "store_business_data": {
        "enabled": True,
        "auto_store": True,
        "validation_required": True,
    },
}

# Agent Behavior Settings
BEHAVIOR_CONFIG = {
    "conversational_style": "professional_friendly",
    "question_pacing": "one_at_a_time",
    "follow_up_enabled": True,
    "data_validation": True,
    "progress_tracking": True,
}
