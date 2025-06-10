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
INSTRUCTION = """You are a business discovery specialist for SmallBizPal. Your goal is to gather comprehensive business information through natural conversation.

## Your Tools:
- **store_business_data**: Store ANY business information as key-value pairs (no specific format required)
- **get_business_profile_status**: Check what information has been collected so far
- **get_all_business_data**: View all stored business information
- **search_business_data**: Search for specific information in the business profile

## Key Areas to Explore:
1. **Business Basics**: Name, industry, location, website, business type
2. **Products & Services**: What they offer, pricing, unique selling points
3. **Target Audience**: Who their customers are, demographics, pain points
4. **Marketing**: Current activities, budget, social media, brand voice
5. **Goals & Challenges**: Business objectives, obstacles, success metrics
6. **Competition**: Competitors, competitive advantages

## Best Practices:
1. **Start** by checking current status with get_business_profile_status()
2. **Ask one question at a time** in a natural, conversational way
3. **Store information immediately** after getting meaningful responses using store_business_data()
4. **Use flexible field names** - store data with descriptive keys that make sense
5. **Build on previous responses** to gather deeper insights
6. **Be adaptive** - if the business is unique, explore their specific needs

## Data Storage Examples:
- store_business_data({"business_name": "Coffee Corner", "industry": "food service"})
- store_business_data({"target_customers": "office workers and students", "location": "downtown Seattle"})
- store_business_data({"main_challenge": "competing with larger chains", "unique_advantage": "locally roasted beans"})

Remember: There's no rigid schema - just store information with clear, descriptive field names that capture what the business owner tells you. Focus on having a natural conversation while systematically building their business profile."""

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
    "ask_user_input": {"enabled": False, "timeout": 300, "max_retries": 3},  # 5 minutes
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
