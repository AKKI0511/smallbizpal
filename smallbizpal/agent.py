"""
SmallBizPal - AI-Powered Small Business Assistant

This is the main entry point for the SmallBizPal ADK multi-agent system.
According to ADK conventions, this file must contain a 'root_agent' variable.
"""

from google.adk.agents import LlmAgent

# from google.adk.tools import google_search  # Will be imported when needed

# For now, we'll create a basic orchestrator agent
# The actual multi-agent implementation will be added later
root_agent = LlmAgent(
    name="smallbizpal_orchestrator",
    model="gemini-2.0-flash-exp",
    description="SmallBizPal Orchestrator - coordinates all business assistance tasks",
    instruction="""You are SmallBizPal, an AI assistant designed to help small businesses with:

    1. Business Discovery: Understanding their business, goals, and target audience
    2. Marketing Generation: Creating marketing materials and content
    3. Customer Engagement: Handling customer interactions and lead management
    4. Performance Reporting: Providing insights and reports on business activities

    You should greet users warmly and help them identify which aspect of their business
    they'd like assistance with. Guide them through the process step by step.""",
    # tools=[],  # Tools will be added as we implement each agent
    # sub_agents=[],  # Sub-agents will be added as we implement the multi-agent system
)

# Export for easy importing
__all__ = ["root_agent"]
