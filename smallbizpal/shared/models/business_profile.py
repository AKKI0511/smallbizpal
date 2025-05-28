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

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class BusinessProfile:
    """Data model for storing comprehensive business information."""

    # Basic business information
    business_name: Optional[str] = None
    industry: Optional[str] = None
    business_type: Optional[str] = None  # LLC, Corp, Sole Proprietorship, etc.
    location: Optional[str] = None
    website: Optional[str] = None

    # Products and services
    products_services: List[str] = field(default_factory=list)
    unique_value_proposition: Optional[str] = None
    pricing_model: Optional[str] = None

    # Target audience
    target_audience: Optional[str] = None
    customer_demographics: Dict[str, Any] = field(default_factory=dict)
    customer_pain_points: List[str] = field(default_factory=list)

    # Brand and messaging
    brand_voice: Optional[str] = None
    brand_personality: Optional[str] = None
    key_messages: List[str] = field(default_factory=list)

    # Business goals and challenges
    business_goals: List[str] = field(default_factory=list)
    challenges: List[str] = field(default_factory=list)
    success_metrics: List[str] = field(default_factory=list)

    # Marketing and digital presence
    current_marketing_activities: List[str] = field(default_factory=list)
    social_media_presence: Dict[str, str] = field(default_factory=dict)
    marketing_budget: Optional[str] = None

    # Competitive landscape
    competitors: List[str] = field(default_factory=list)
    competitive_advantages: List[str] = field(default_factory=list)

    # Metadata
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    completion_status: Dict[str, bool] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the business profile to a dictionary."""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
        return result

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BusinessProfile":
        """Create a BusinessProfile from a dictionary."""
        # Handle datetime fields
        if "created_at" in data and isinstance(data["created_at"], str):
            data["created_at"] = datetime.fromisoformat(data["created_at"])
        if "updated_at" in data and isinstance(data["updated_at"], str):
            data["updated_at"] = datetime.fromisoformat(data["updated_at"])

        return cls(**data)

    def update_field(self, field_name: str, value: Any) -> None:
        """Update a specific field and timestamp."""
        if hasattr(self, field_name):
            setattr(self, field_name, value)
            self.updated_at = datetime.now()
            self.completion_status[field_name] = True
