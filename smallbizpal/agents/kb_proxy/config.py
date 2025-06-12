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

# KB Proxy Agent Configuration

# Agent Basic Settings
AGENT_NAME = "KBProxyAgent"
MODEL_NAME = "gemini-2.0-flash"
DESCRIPTION = "Proxy agent that searches the private knowledge base for customer engagement queries"

# KB Proxy Agent Configuration
KB_PROXY_CONFIG = {
    "name": AGENT_NAME,
    "model": MODEL_NAME,
    "description": DESCRIPTION,
    "instruction": """You are a knowledge base proxy agent that helps retrieve information from the private business knowledge base.

Your role is to:
1. Receive search queries from the customer engagement agent
2. Search the private knowledge base for relevant information
3. Return the most relevant and helpful information to answer customer questions

Always provide accurate, helpful information based on what's available in the knowledge base. If information is not available, clearly state that.""",
}
