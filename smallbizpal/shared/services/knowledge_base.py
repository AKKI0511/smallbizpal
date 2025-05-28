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
from typing import Any, Dict, Optional

from smallbizpal.shared.models.business_profile import BusinessProfile


class KnowledgeBaseService:
    """Simple file-based knowledge base for storing and retrieving business data."""

    def __init__(self, storage_path: str = "data/knowledge_base.json"):
        """Initialize the knowledge base service.

        Args:
            storage_path: Path to the JSON file for data storage
        """
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self._data = self._load_data()

    def _load_data(self) -> Dict[str, Any]:
        """Load data from storage file."""
        if self.storage_path.exists():
            try:
                with open(self.storage_path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        return {
            "business_profile": {},
            "marketing_assets": [],
            "customer_interactions": [],
            "performance_data": {},
        }

    def _save_data(self) -> None:
        """Save data to storage file."""
        with open(self.storage_path, "w") as f:
            json.dump(self._data, f, indent=2, default=str)

    def store_business_profile(self, profile_data: Dict[str, Any]) -> None:
        """Store or update business profile information.

        Args:
            profile_data: Dictionary containing business profile data
        """
        # Update existing profile or create new one
        current_profile = self._data.get("business_profile", {})
        current_profile.update(profile_data)
        self._data["business_profile"] = current_profile
        self._save_data()

    def get_business_profile(self) -> Optional[BusinessProfile]:
        """Retrieve the current business profile.

        Returns:
            BusinessProfile object or None if no profile exists
        """
        profile_data = self._data.get("business_profile")
        if profile_data:
            return BusinessProfile.from_dict(profile_data)
        return None

    def store_marketing_asset(self, asset_data: Dict[str, Any]) -> None:
        """Store marketing asset information.

        Args:
            asset_data: Dictionary containing marketing asset data
        """
        if "marketing_assets" not in self._data:
            self._data["marketing_assets"] = []

        asset_data["created_at"] = str(asset_data.get("created_at", ""))
        self._data["marketing_assets"].append(asset_data)
        self._save_data()

    def get_marketing_assets(self) -> list[Dict[str, Any]]:
        """Retrieve all marketing assets.

        Returns:
            List of marketing asset dictionaries
        """
        return self._data.get("marketing_assets", [])

    def store_customer_interaction(self, interaction_data: Dict[str, Any]) -> None:
        """Store customer interaction data.

        Args:
            interaction_data: Dictionary containing interaction data
        """
        if "customer_interactions" not in self._data:
            self._data["customer_interactions"] = []

        interaction_data["timestamp"] = str(interaction_data.get("timestamp", ""))
        self._data["customer_interactions"].append(interaction_data)
        self._save_data()

    def get_customer_interactions(self) -> list[Dict[str, Any]]:
        """Retrieve all customer interactions.

        Returns:
            List of interaction dictionaries
        """
        return self._data.get("customer_interactions", [])

    def store_performance_data(self, metric_name: str, data: Dict[str, Any]) -> None:
        """Store performance metric data.

        Args:
            metric_name: Name of the performance metric
            data: Performance data dictionary
        """
        if "performance_data" not in self._data:
            self._data["performance_data"] = {}

        self._data["performance_data"][metric_name] = data
        self._save_data()

    def get_performance_data(self, metric_name: Optional[str] = None) -> Dict[str, Any]:
        """Retrieve performance data.

        Args:
            metric_name: Specific metric name, or None for all metrics

        Returns:
            Performance data dictionary
        """
        performance_data = self._data.get("performance_data", {})
        if metric_name:
            return performance_data.get(metric_name, {})
        return performance_data

    def clear_all_data(self) -> None:
        """Clear all stored data (for testing/reset purposes)."""
        self._data = {
            "business_profile": {},
            "marketing_assets": [],
            "customer_interactions": [],
            "performance_data": {},
        }
        self._save_data()


# Global singleton instance
knowledge_base_service = KnowledgeBaseService()
