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

from google.adk.tools.agent_tool import AgentTool

# Import the proxy agent that has access to the private KB
from smallbizpal.agents.kb_proxy import kb_proxy_agent

# TODO: Remove this once we have a proper A2A implementation
# def ask_internal_kb(query: str) -> str:
#     """
#     Asks the internal knowledge base for information about the business.
#     This uses A2A communication to securely access private business data.

#     Args:
#         query: The customer's question about the business.

#     Returns:
#         Relevant information from the internal knowledge base.
#     """
#     try:
#         # For MVP, we'll use a direct call to the KB proxy
#         # In production, this would use A2A protocol
#         from smallbizpal.agents.kb_proxy.tools import search_private_kb
#         return search_private_kb(query)
#     except Exception as e:
#         return f"I apologize, but I'm having trouble accessing our business information right now. Please try again later or contact us directly. Error: {str(e)}"

ask_internal_kb = AgentTool(agent=kb_proxy_agent)
