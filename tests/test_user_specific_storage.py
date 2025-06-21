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

import shutil
import tempfile
from pathlib import Path

import pytest

from smallbizpal.shared.services.knowledge_base import KnowledgeBaseService


def test_user_specific_storage():
    """Test that data is stored separately for different users."""

    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Initialize knowledge base service with temp directory
        kb_service = KnowledgeBaseService(base_storage_path=temp_dir)

        # Test data for two different users
        user1_id = "user1"
        user2_id = "user2"

        user1_data = {"company_name": "User1 Corp", "industry": "tech"}
        user2_data = {"company_name": "User2 Inc", "industry": "finance"}

        # Store data for both users
        result1 = kb_service.update_business_profile(user1_id, user1_data)
        result2 = kb_service.update_business_profile(user2_id, user2_data)

        # Verify both operations succeeded
        assert result1["status"] == "success"
        assert result2["status"] == "success"

        # Retrieve data for both users
        profile1 = kb_service.get_business_profile(user1_id)
        profile2 = kb_service.get_business_profile(user2_id)

        # Verify data is correctly separated
        assert profile1 is not None
        assert profile2 is not None

        data1 = profile1.get_all_data()
        data2 = profile2.get_all_data()

        assert data1["company_name"] == "User1 Corp"
        assert data1["industry"] == "tech"

        assert data2["company_name"] == "User2 Inc"
        assert data2["industry"] == "finance"

        # Verify files are created in separate directories
        user1_path = Path(temp_dir) / user1_id / "knowledge_base.json"
        user2_path = Path(temp_dir) / user2_id / "knowledge_base.json"

        assert user1_path.exists()
        assert user2_path.exists()

        # Verify no cross-contamination
        profile1_cross = kb_service.get_business_profile(user2_id)
        data1_cross = profile1_cross.get_all_data()
        assert data1_cross["company_name"] != "User1 Corp"


def test_marketing_assets_user_separation():
    """Test that marketing assets are stored separately for different users."""

    with tempfile.TemporaryDirectory() as temp_dir:
        kb_service = KnowledgeBaseService(base_storage_path=temp_dir)

        user1_id = "user1"
        user2_id = "user2"

        # Store marketing assets for both users
        asset1 = {"content": "User1 content", "platform": "twitter"}
        asset2 = {"content": "User2 content", "platform": "linkedin"}

        kb_service.store_marketing_asset(user1_id, asset1)
        kb_service.store_marketing_asset(user2_id, asset2)

        # Retrieve assets for both users
        assets1 = kb_service.get_marketing_assets(user1_id)
        assets2 = kb_service.get_marketing_assets(user2_id)

        # Verify separation
        assert len(assets1) == 1
        assert len(assets2) == 1

        assert assets1[0]["content"] == "User1 content"
        assert assets2[0]["content"] == "User2 content"


def test_customer_interactions_user_separation():
    """Test that customer interactions are stored separately for different users."""

    with tempfile.TemporaryDirectory() as temp_dir:
        kb_service = KnowledgeBaseService(base_storage_path=temp_dir)

        user1_id = "user1"
        user2_id = "user2"

        # Store interactions for both users
        interaction1 = {"type": "meeting_request", "customer_name": "John Doe"}
        interaction2 = {"type": "inquiry", "customer_name": "Jane Smith"}

        kb_service.store_customer_interaction(user1_id, interaction1)
        kb_service.store_customer_interaction(user2_id, interaction2)

        # Retrieve interactions for both users
        interactions1 = kb_service.get_customer_interactions(user1_id)
        interactions2 = kb_service.get_customer_interactions(user2_id)

        # Verify separation
        assert len(interactions1) == 1
        assert len(interactions2) == 1

        assert interactions1[0]["customer_name"] == "John Doe"
        assert interactions2[0]["customer_name"] == "Jane Smith"


def test_performance_data_user_separation():
    """Test that performance data is stored separately for different users."""

    with tempfile.TemporaryDirectory() as temp_dir:
        kb_service = KnowledgeBaseService(base_storage_path=temp_dir)

        user1_id = "user1"
        user2_id = "user2"

        # Store performance data for both users
        perf1 = {"leads": 10, "conversions": 2}
        perf2 = {"leads": 5, "conversions": 1}

        kb_service.store_performance_data(user1_id, "monthly_metrics", perf1)
        kb_service.store_performance_data(user2_id, "monthly_metrics", perf2)

        # Retrieve performance data for both users
        data1 = kb_service.get_performance_data(user1_id, "monthly_metrics")
        data2 = kb_service.get_performance_data(user2_id, "monthly_metrics")

        # Verify separation
        assert data1["leads"] == 10
        assert data2["leads"] == 5


if __name__ == "__main__":
    pytest.main([__file__])
