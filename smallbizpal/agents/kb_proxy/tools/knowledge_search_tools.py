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

import json
from pathlib import Path


def search_private_kb(query: str) -> str:
    """
    Searches the private knowledge base for information relevant to the query.

    For MVP, this simply returns the entire business profile data.
    Later this will be upgraded to vector search with RAG.

    Args:
        query: The search query from the customer engagement agent

    Returns:
        Complete business profile data from the knowledge base
    """
    try:
        # Load the private knowledge base
        kb_path = Path("data/knowledge_base.json")
        if not kb_path.exists():
            return "Knowledge base not found. Please ensure business profile is set up."

        with open(kb_path, "r") as f:
            kb_data = json.load(f)

        # Extract business profile data
        business_profile = kb_data.get("business_profile", {}).get("data", {})

        if not business_profile:
            return "No business information available. Please complete the business profile setup."

        # For MVP: Simply return the entire business profile as JSON string
        return json.dumps(business_profile, indent=2)

    except Exception as e:
        return f"Error accessing knowledge base: {str(e)}"
