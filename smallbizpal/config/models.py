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


# Global model configurations for SmallBizPal

# Available models in the system
AVAILABLE_MODELS = ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash"]

# Default model for the application
DEFAULT_MODEL = "gemini-2.5-flash"

# Global model parameter configurations
MODEL_CONFIGS = {
    "default": {
        "temperature": 0.7,
        "max_output_tokens": 2048,
        "top_p": 0.8,
        "top_k": 40,
    },
    "creative": {
        "temperature": 0.9,
        "max_output_tokens": 2048,
        "top_p": 0.9,
        "top_k": 40,
    },
    "analytical": {
        "temperature": 0.3,
        "max_output_tokens": 1024,
        "top_p": 0.7,
        "top_k": 20,
    },
    "precise": {
        "temperature": 0.1,
        "max_output_tokens": 1024,
        "top_p": 0.5,
        "top_k": 10,
    },
}


def get_model_config(config_type: str = "default") -> dict:
    """Get model configuration parameters.

    Args:
        config_type: Type of configuration (default, creative, analytical, precise)

    Returns:
        Dictionary of model parameters
    """
    return MODEL_CONFIGS.get(config_type, MODEL_CONFIGS["default"])
