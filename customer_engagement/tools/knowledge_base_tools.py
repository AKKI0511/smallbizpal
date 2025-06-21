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
from google.adk.tools import ToolContext

# Import the proxy agent that has access to the private KB
from smallbizpal.agents.kb_proxy import kb_proxy_agent


# TODO: Remove this once we have a proper A2A implementation
def ask_internal_kb(query: str, tool_context: ToolContext) -> str:
    """
    Asks the internal knowledge base for information about the business.
    This uses A2A communication to securely access private business data.

    Args:
        query: The customer's question about the business.

    Returns:
        Relevant information from the internal knowledge base.
    """
    try:
        # For MVP, we'll use a direct call to the KB proxy
        # In production, this would use A2A protocol
        from smallbizpal.agents.kb_proxy.tools import search_private_kb
        return search_private_kb(query, tool_context)
    except Exception as e:
        return f"I apologize, but I'm having trouble accessing our business information right now. Please try again later or contact us directly. Error: {str(e)}"

# ask_internal_kb = AgentTool(agent=kb_proxy_agent)


# # TODO: The A2A_HOST should be a configurable setting, not hardcoded.
# # In a real-world scenario, this would come from a config file or env variable.
# _KB_PROXY_A2A_HOST = "http://localhost:8000"


# async def ask_internal_kb(query: str, tool_context: ToolContext) -> str:
#     """
#     Asks the internal knowledge base for information about the business.
#     This uses A2A communication to securely access private business data.

#     Args:
#         query: The customer's question about the business.

#     Returns:
#         Relevant information from the internal knowledge base.
#     """
#     if not tool_context:
#         return "ERROR: ToolContext is not available. Cannot determine user."

#     user_id = tool_context.get_user_id()
#     if not user_id:
#         return "ERROR: user_id not found in ToolContext."

#     try:
#         a2a_client = A2AClient()
#         # The kb_proxy_agent is made available as a remote agent via A2A.
#         # We pass the user_id in the invocation_context so the remote agent
#         # knows which user's data to access.
#         response_events = a2a_client.send_task(
#             host_info=A2AHostInfo(
#                 hostname=_KB_PROXY_A2A_HOST, agent_name="kb_proxy_agent"
#             ),
#             query=query,
#             invocation_context={"user_id": user_id},
#         )

#         final_response = ""
#         async for event in response_events:
#             if event.is_final_response() and event.content:
#                 final_response = "".join(
#                     part.text for part in event.content.parts if part.text
#                 )
#         return (
#             final_response
#             or "I found some information, but couldn't form a response."
#         )

#     except Exception as e:
#         return f"I apologize, but I'm having trouble accessing our business information right now. Please try again later or contact us directly. Error: {str(e)}"


# # This tool is now a standard function tool that internally uses A2A.
# ask_internal_kb_tool = AgentTool.from_function(
#     impl_fn=ask_internal_kb,
#     name="ask_internal_kb",
#     description="Asks the internal knowledge base for information about the business. Use this for any customer questions about the business itself, its products, or its services.",
#     tool_context_serializer=default_tool_context_serializer(),
# )

# TODO: Direct agent call in function
# import os
# from google.adk.agents import AgentTool
# from google.adk.tools import ToolContext, default_tool_context_serializer
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.genai import types

# # Import the agent we want to invoke programmatically
# from smallbizpal.agents.kb_proxy import kb_proxy_agent


# async def ask_internal_kb(query: str, tool_context: ToolContext) -> str:
#     """
#     Asks the internal knowledge base for information about the business.
#     This programmatically invokes the kb_proxy_agent with a specific
#     user_id to ensure the correct business data is accessed.

#     Args:
#         query: The customer's question about the business.
#         tool_context: The tool context from the customer-facing agent.

#     Returns:
#         Relevant information from the internal knowledge base.
#     """
#     try:
#         session_service = InMemorySessionService()
#         runner = Runner(
#             app_name="kb_proxy_runner_app",
#             agent=kb_proxy_agent,
#             session_service=session_service,
#         )
#         user_id = tool_context._invocation_context.session.user_id

#         # Create a new session with the BUSINESS_OWNER_ID to fetch the
#         # correct data. The session for this run is ephemeral.
#         session = await runner.session_service.create_session(
#             app_name="kb_proxy_runner_app", user_id=user_id
#         )

#         message = types.Content(role="user", parts=[types.Part(text=query)])

#         response_events = runner.run_async(
#             session_id=session.id, user_id=session.user_id, new_message=message
#         )

#         final_response = ""
#         async for event in response_events:
#             if event.is_final_response() and event.content:
#                 final_response = "".join(
#                     part.text for part in event.content.parts if part.text
#                 )

#         return (
#             final_response
#             or "I couldn't find a specific answer, but I can try to help with something else."
#         )

#     except Exception as e:
#         return f"I apologize, but I'm having trouble accessing our business information right now. Please try again later or contact us directly. Error: {str(e)}"
