"""
Basic tests to verify SmallBizPal project structure and imports.
"""

import pytest

from smallbizpal.agent import root_agent


def test_root_agent_exists():
    """Test that the root_agent is properly defined."""
    assert root_agent is not None
    assert hasattr(root_agent, "name")
    assert root_agent.name == "smallbizpal_orchestrator"


def test_package_imports():
    """Test that all main packages can be imported."""
    # Test main package
    import smallbizpal

    # Test shared packages
    # Test agent packages (should not fail even if empty)
    from smallbizpal import agents, callbacks, config, shared
    from smallbizpal.agents import (
        business_discovery,
        customer_engagement,
        marketing_generator,
        orchestrator,
        performance_reporting,
    )

    # All imports should succeed
    assert True  # If we get here, all imports worked


if __name__ == "__main__":
    pytest.main([__file__])
