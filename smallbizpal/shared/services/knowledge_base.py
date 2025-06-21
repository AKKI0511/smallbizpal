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
from typing import Any, Dict, List, Optional

from smallbizpal.shared.models.business_profile import BusinessProfile


class KnowledgeBaseService:
    """Simple file-based knowledge base for storing and retrieving business data."""

    def __init__(self, base_storage_path: str = "data"):
        """Initialize the knowledge base service.

        Args:
            base_storage_path: Path to the directory for data storage
        """
        self.base_storage_path = Path(base_storage_path)

    def _get_storage_path(self, user_id: str) -> Path:
        """Get the storage path for a specific user."""
        storage_path = self.base_storage_path / user_id / "knowledge_base.json"
        storage_path.parent.mkdir(parents=True, exist_ok=True)
        return storage_path

    def _load_data(self, user_id: str) -> Dict[str, Any]:
        """Load data from a user's storage file."""
        storage_path = self._get_storage_path(user_id)
        if storage_path.exists():
            try:
                with open(storage_path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        return {
            "business_profile": {},
            "marketing_assets": [],
            "customer_interactions": [],
            "performance_data": {},
        }

    def _save_data(self, user_id: str, data: Dict[str, Any]) -> None:
        """Save data to a user's storage file."""
        storage_path = self._get_storage_path(user_id)

        def json_serializer(obj):
            """Custom JSON serializer for datetime and other objects."""
            if hasattr(obj, "isoformat"):
                return obj.isoformat()
            elif hasattr(obj, "model_dump"):
                return obj.model_dump()
            elif hasattr(obj, "__dict__"):
                return obj.__dict__
            return str(obj)

        with open(storage_path, "w") as f:
            json.dump(data, f, indent=2, default=json_serializer)

    def update_business_profile(
        self, user_id: str, new_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Update business profile with any new data for a specific user.

        Args:
            user_id: The ID of the user.
            new_data: Dictionary containing any business information

        Returns:
            Dictionary with update status and information
        """
        try:
            data = self._load_data(user_id)
            profile = self.get_business_profile(user_id)
            if profile is None:
                profile = BusinessProfile()

            profile.update_data(new_data)
            data["business_profile"] = profile.model_dump()
            self._save_data(user_id, data)

            return {
                "status": "success",
                "message": f"Successfully updated business profile with {len(new_data)} new fields",
                "updated_fields": list(new_data.keys()),
                "total_fields": len(profile.data),
                "total_updates": profile.total_updates,
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error updating business profile: {str(e)}",
                "updated_fields": [],
                "total_fields": 0,
            }

    def get_business_profile(self, user_id: str) -> Optional[BusinessProfile]:
        """Retrieve the current business profile for a specific user.

        Args:
            user_id: The ID of the user.

        Returns:
            BusinessProfile object or None if no profile exists
        """
        data = self._load_data(user_id)
        profile_data = data.get("business_profile")
        if profile_data:
            try:
                return BusinessProfile.model_validate(profile_data)
            except Exception:
                return BusinessProfile(data=profile_data)
        return None

    def get_business_data(self, user_id: str) -> Dict[str, Any]:
        """Get all business data for a specific user as a simple dictionary.

        Args:
            user_id: The ID of the user.

        Returns:
            All business data or empty dict if no profile exists
        """
        profile = self.get_business_profile(user_id)
        if profile:
            return profile.get_all_data()
        return {}

    def search_business_data(
        self, user_id: str, search_terms: List[str]
    ) -> Dict[str, Any]:
        """Search business data for specific terms for a given user.

        Args:
            user_id: The ID of the user.
            search_terms: List of terms to search for

        Returns:
            Dictionary of matching business data
        """
        profile = self.get_business_profile(user_id)
        if profile:
            return profile.search_data(search_terms)
        return {}

    def get_profile_summary(self, user_id: str) -> Dict[str, Any]:
        """Get a summary of the current business profile for a specific user.

        Args:
            user_id: The ID of the user.

        Returns:
            Summary information about the profile
        """
        profile = self.get_business_profile(user_id)
        if profile:
            summary = profile.get_summary()
            summary["profile_exists"] = True
            return summary
        else:
            return {
                "profile_exists": False,
                "total_fields": 0,
                "has_data": False,
                "message": "No business profile exists yet",
            }

    def store_business_profile(
        self, user_id: str, profile_data: Dict[str, Any]
    ) -> None:
        """Legacy method - redirects to update_business_profile."""
        self.update_business_profile(user_id, profile_data)

    def store_marketing_asset(self, user_id: str, asset_data: Dict[str, Any]) -> None:
        """Store marketing asset information for a specific user."""
        data = self._load_data(user_id)
        if "marketing_assets" not in data:
            data["marketing_assets"] = []

        asset_data["created_at"] = str(asset_data.get("created_at", ""))
        data["marketing_assets"].append(asset_data)
        self._save_data(user_id, data)

    def get_marketing_assets(self, user_id: str) -> list[Dict[str, Any]]:
        """Retrieve all marketing assets for a specific user.

        Args:
            user_id: The ID of the user.

        Returns:
            List of marketing asset dictionaries
        """
        data = self._load_data(user_id)
        return data.get("marketing_assets", [])

    def store_customer_interaction(
        self, user_id: str, interaction_data: Dict[str, Any]
    ) -> None:
        """Store customer interaction data for a specific user.

        Args:
            user_id: The ID of the user.
            interaction_data: Dictionary containing interaction data
        """
        data = self._load_data(user_id)
        if "customer_interactions" not in data:
            data["customer_interactions"] = []

        interaction_data["timestamp"] = str(interaction_data.get("timestamp", ""))
        data["customer_interactions"].append(interaction_data)
        self._save_data(user_id, data)

    def get_customer_interactions(self, user_id: str) -> list[Dict[str, Any]]:
        """Retrieve all customer interactions for a specific user.

        Args:
            user_id: The ID of the user.

        Returns:
            List of interaction dictionaries
        """
        data = self._load_data(user_id)
        return data.get("customer_interactions", [])

    def store_performance_data(
        self, user_id: str, metric_name: str, metric_data: Dict[str, Any]
    ) -> None:
        """Store performance metric data for a specific user.

        Args:
            user_id: The ID of the user.
            metric_name: Name of the performance metric
            metric_data: Performance data dictionary
        """
        data = self._load_data(user_id)
        if "performance_data" not in data:
            data["performance_data"] = {}

        data["performance_data"][metric_name] = metric_data
        self._save_data(user_id, data)

    def get_performance_data(
        self, user_id: str, metric_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Retrieve performance data for a specific user.

        Args:
            user_id: The ID of the user.
            metric_name: Specific metric name, or None for all metrics

        Returns:
            Performance data dictionary
        """
        data = self._load_data(user_id)
        performance_data = data.get("performance_data", {})
        if metric_name:
            return performance_data.get(metric_name, {})
        return performance_data

    def clear_all_data(self, user_id: str) -> None:
        """Clear all stored data for a specific user (for testing/reset purposes)."""
        data = {
            "business_profile": {},
            "marketing_assets": [],
            "customer_interactions": [],
            "performance_data": {},
        }
        self._save_data(user_id, data)


# Global singleton instance
knowledge_base_service = KnowledgeBaseService()
