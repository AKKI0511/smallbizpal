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

import os
from typing import Optional

# API Keys and Authentication
GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")

# Application Settings
APP_NAME = "SmallBizPal"
APP_VERSION = "0.1.0"
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Storage Settings
DATA_DIRECTORY = os.getenv("DATA_DIRECTORY", "data")
KNOWLEDGE_BASE_FILE = os.path.join(DATA_DIRECTORY, "knowledge_base.json")

# ADK Settings
ADK_WEB_PORT = int(os.getenv("ADK_WEB_PORT", "8000"))
ADK_LOG_LEVEL = os.getenv("ADK_LOG_LEVEL", "INFO")

# Agent Settings
DEFAULT_AGENT_TIMEOUT = int(os.getenv("DEFAULT_AGENT_TIMEOUT", "300"))  # 5 minutes
MAX_AGENT_ITERATIONS = int(os.getenv("MAX_AGENT_ITERATIONS", "10"))


# Validate required settings
def validate_settings() -> None:
    """Validate that required settings are present."""
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable is required")


# Optional: Auto-validate on import in development
if DEBUG:
    try:
        validate_settings()
    except ValueError as e:
        print(f"Warning: {e}")
