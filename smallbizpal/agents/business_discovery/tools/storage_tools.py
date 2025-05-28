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

from typing import Any, Dict


def store_business_data(data: Dict[str, Any]) -> str:
    """Store business information in the knowledge base.

    Args:
        data: Dictionary containing business information to store

    Returns:
        Confirmation message of successful storage
    """
    # Import here to avoid circular imports
    from smallbizpal.shared.services.knowledge_base import knowledge_base_service

    try:
        knowledge_base_service.store_business_profile(data)
        return f"Successfully stored business data: {list(data.keys())}"
    except Exception as e:
        return f"Error storing business data: {str(e)}"
