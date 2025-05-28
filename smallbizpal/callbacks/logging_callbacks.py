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

from smallbizpal.shared.utils.logging import logger


def log_agent_start(agent_name: str, input_data: str) -> None:
    """Log when an agent starts processing."""
    logger.info(f"Agent {agent_name} started processing: {input_data[:100]}...")


def log_agent_complete(agent_name: str, output_data: str) -> None:
    """Log when an agent completes processing."""
    logger.info(f"Agent {agent_name} completed processing: {output_data[:100]}...")


def log_tool_call(tool_name: str, parameters: dict) -> None:
    """Log when a tool is called."""
    logger.debug(f"Tool {tool_name} called with parameters: {parameters}")


def log_error(agent_name: str, error: Exception) -> None:
    """Log errors that occur during agent processing."""
    logger.error(f"Error in agent {agent_name}: {str(error)}")
