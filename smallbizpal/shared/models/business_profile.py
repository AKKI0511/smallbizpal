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

from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel, Field


class BusinessProfile(BaseModel):
    """Comprehensive business profile model optimized for LLM interactions."""

    # Core flexible data storage - this is where everything goes
    data: Dict[str, Any] = Field(
        default_factory=dict,
        description="All business information stored as flexible key-value pairs",
    )

    # Metadata
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    total_updates: int = Field(
        default=0, description="Number of times profile has been updated"
    )

    def update_data(self, new_data: Dict[str, Any]) -> None:
        """Update business data with new information.

        Args:
            new_data: Dictionary with any business information
        """
        self.data.update(new_data)
        self.updated_at = datetime.now()
        self.total_updates += 1

    def get_all_data(self) -> Dict[str, Any]:
        """Get all stored business data.

        Returns:
            All business data as dictionary
        """
        return self.data.copy()

    def search_data(self, search_terms: List[str]) -> Dict[str, Any]:
        """Search for data containing specific terms.

        Args:
            search_terms: List of terms to search for in keys or values

        Returns:
            Dictionary of matching key-value pairs
        """
        results = {}
        search_terms_lower = [term.lower() for term in search_terms]

        for key, value in self.data.items():
            key_lower = key.lower()
            value_str = str(value).lower()

            # Check if any search term appears in key or value
            if any(
                term in key_lower or term in value_str for term in search_terms_lower
            ):
                results[key] = value

        return results

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the business profile.

        Returns:
            Summary information about the profile
        """
        return {
            "total_fields": len(self.data),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "total_updates": self.total_updates,
            "sample_fields": list(self.data.keys())[:10],  # First 10 field names
            "has_data": len(self.data) > 0,
        }
