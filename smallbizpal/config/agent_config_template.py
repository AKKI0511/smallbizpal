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
Agent Configuration Template

Copy this file to your agent folder as config.py and customize the values below.
This template provides a standardized structure for agent configuration.
"""

# ============================================================================
# AGENT BASIC SETTINGS
# ============================================================================

# Agent identification
AGENT_NAME = "YourAgentName"  # Should match the class name
MODEL_NAME = "gemini-2.5-flash"  # or "gemini-2.5-pro" for more complex tasks
DESCRIPTION = "Brief description of what this agent does"

# Agent Instructions/System Prompt
INSTRUCTION = """You are [agent role description].

Your responsibilities include:
1. [Primary responsibility]
2. [Secondary responsibility]
3. [Additional responsibilities]

Key behaviors:
- [Behavior 1]
- [Behavior 2]
- [Behavior 3]

Always [important guidelines for the agent]."""

# ============================================================================
# AGENT BEHAVIOR CONFIGURATION
# ============================================================================

# General behavior settings
BEHAVIOR_CONFIG = {
    "conversational_style": "professional_friendly",  # professional_friendly, casual, formal
    "response_length": "medium",  # short, medium, long
    "proactive": True,  # Whether agent should proactively suggest actions
    "follow_up_enabled": True,  # Whether to ask follow-up questions
    "validation_required": True,  # Whether to validate inputs/outputs
    "progress_tracking": True,  # Whether to track and report progress
}

# Task-specific settings
TASK_CONFIG = {
    "max_iterations": 10,  # Maximum number of task iterations
    "timeout": 300,  # Task timeout in seconds (5 minutes)
    "retry_attempts": 3,  # Number of retry attempts for failed operations
    "auto_save": True,  # Whether to automatically save progress
    "confirmation_required": False,  # Whether to ask for user confirmation
}

# ============================================================================
# TOOLS CONFIGURATION
# ============================================================================

# Tool enablement and configuration
TOOLS_CONFIG = {
    "example_tool": {
        "enabled": True,
        "timeout": 30,
        "max_retries": 3,
        "auto_execute": False,
    },
    # Add more tools as needed
}

# ============================================================================
# DOMAIN-SPECIFIC CONFIGURATION
# ============================================================================

# Add domain-specific configuration sections here
# For example:

# Data processing settings
DATA_CONFIG = {
    "input_validation": True,
    "output_format": "json",
    "storage_enabled": True,
    "backup_enabled": True,
}

# Integration settings
INTEGRATION_CONFIG = {
    "external_apis": [],
    "webhooks_enabled": False,
    "notifications_enabled": True,
}

# ============================================================================
# PROMPTS AND TEMPLATES
# ============================================================================

# Common prompts used by the agent
PROMPTS = {
    "welcome": "Hello! I'm here to help you with [agent purpose]. How can I assist you today?",
    "error": "I apologize, but I encountered an error. Let me try a different approach.",
    "completion": "I've completed the task successfully. Is there anything else you'd like me to help with?",
    "clarification": "Could you please provide more details about [specific aspect]?",
}

# Template messages or responses
TEMPLATES = {
    "status_update": "Progress update: {progress}% complete. Current step: {current_step}",
    "result_summary": "Task completed. Summary: {summary}. Next steps: {next_steps}",
}

# ============================================================================
# VALIDATION AND CONSTRAINTS
# ============================================================================

# Input validation rules
VALIDATION_RULES = {
    "required_fields": [],  # List of required input fields
    "field_types": {},  # Dictionary of field name -> expected type
    "value_ranges": {},  # Dictionary of field name -> (min, max) values
    "allowed_values": {},  # Dictionary of field name -> list of allowed values
}

# Agent constraints and limits
CONSTRAINTS = {
    "max_response_length": 2000,  # Maximum characters in response
    "max_tool_calls": 5,  # Maximum tool calls per interaction
    "rate_limit": 60,  # Maximum requests per minute
    "memory_limit": "100MB",  # Maximum memory usage
}
