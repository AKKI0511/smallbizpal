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
SmallBizPal Global Configuration Module

This module provides global configuration settings and utilities.
Individual agents manage their own configuration in their respective config.py files.

Global config provides:
- Application settings (API keys, ports, etc.)
- Model configurations and utilities
- Business domain constants
- Shared utilities
"""

from .constants import (
    AGENT_TYPES,
    BUSINESS_CATEGORIES,
    CUSTOMER_SEGMENTS,
    MARKETING_CHANNELS,
    PERFORMANCE_METRICS,
)
from .models import AVAILABLE_MODELS, DEFAULT_MODEL, MODEL_CONFIGS, get_model_config
from .settings import (
    ADK_LOG_LEVEL,
    ADK_WEB_PORT,
    APP_NAME,
    APP_VERSION,
    DATA_DIRECTORY,
    DEBUG,
    DEFAULT_AGENT_TIMEOUT,
    GOOGLE_API_KEY,
    KNOWLEDGE_BASE_FILE,
    MAX_AGENT_ITERATIONS,
    validate_settings,
)

__all__ = [
    # Settings
    "GOOGLE_API_KEY",
    "APP_NAME",
    "APP_VERSION",
    "DEBUG",
    "DATA_DIRECTORY",
    "KNOWLEDGE_BASE_FILE",
    "ADK_WEB_PORT",
    "ADK_LOG_LEVEL",
    "DEFAULT_AGENT_TIMEOUT",
    "MAX_AGENT_ITERATIONS",
    "validate_settings",
    # Models
    "AVAILABLE_MODELS",
    "DEFAULT_MODEL",
    "MODEL_CONFIGS",
    "get_model_config",
    # Constants
    "AGENT_TYPES",
    "BUSINESS_CATEGORIES",
    "MARKETING_CHANNELS",
    "CUSTOMER_SEGMENTS",
    "PERFORMANCE_METRICS",
]
