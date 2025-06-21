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
Basic tests to verify SmallBizPal project structure and imports.
"""

import pytest

from smallbizpal.agent import AGENT_NAME, root_agent


def test_root_agent_exists():
    """Test that the root_agent is properly defined."""
    assert root_agent is not None
    assert hasattr(root_agent, "name")
    assert root_agent.name == AGENT_NAME


def test_package_imports():
    """Test that all main packages can be imported."""
    # Test main package
    import smallbizpal

    # Test shared packages
    # Test agent packages (should not fail even if empty)
    from smallbizpal import agents, callbacks, config, shared
    from smallbizpal.agents import (
        business_discovery,
        kb_proxy,
        marketing_generator,
        performance_reporting,
    )

    # All imports should succeed
    assert True  # If we get here, all imports worked


if __name__ == "__main__":
    pytest.main([__file__])
