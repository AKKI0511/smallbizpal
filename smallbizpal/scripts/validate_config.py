#!/usr/bin/env python3
"""
Configuration Validation Script

This script validates that all agent configurations are properly set up
and can be loaded without errors.
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


def validate_agent_config(agent_name, agent_module_path):
    """Validate a single agent's configuration."""
    print(f"\n🔍 Validating {agent_name}...")

    try:
        # Import the agent module
        module = __import__(agent_module_path, fromlist=[""])

        # Check if the agent has a config
        if hasattr(module, "config"):
            config = module.config

            # Check required config attributes
            required_attrs = ["AGENT_NAME", "MODEL_NAME", "DESCRIPTION", "INSTRUCTION"]
            missing_attrs = []

            for attr in required_attrs:
                if not hasattr(config, attr):
                    missing_attrs.append(attr)

            if missing_attrs:
                print(f"  ❌ Missing required config attributes: {missing_attrs}")
                return False
            else:
                print("  ✅ All required config attributes present")
                print(f"     - Name: {config.AGENT_NAME}")
                print(f"     - Model: {config.MODEL_NAME}")
                print(f"     - Description: {config.DESCRIPTION[:50]}...")

        # Try to import the agent itself
        if hasattr(module, "agent"):
            agent_module = module.agent
            agent_name_attr = f"{agent_name.lower().replace(' ', '_')}_agent"

            if hasattr(agent_module, agent_name_attr):
                agent = getattr(agent_module, agent_name_attr)
                print("  ✅ Agent instance created successfully")
                print(f"     - Agent name: {agent.name}")
                print(f"     - Model: {agent.model}")
                print(f"     - Tools: {len(agent.tools) if agent.tools else 0}")
                return True
            else:
                print(f"  ❌ Agent instance '{agent_name_attr}' not found")
                return False
        else:
            print("  ❌ Agent module not found")
            return False

    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return False


def validate_global_config():
    """Validate global configuration."""
    print("🔍 Validating global configuration...")

    try:
        from smallbizpal.config import (
            APP_NAME,
            APP_VERSION,
            GOOGLE_API_KEY,
        )

        print("  ✅ Global config imports successful")
        print(f"     - App: {APP_NAME} v{APP_VERSION}")
        print(f"     - API Key configured: {'Yes' if GOOGLE_API_KEY else 'No'}")
        return True

    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return False


def validate_main_agent():
    """Validate the main root agent."""
    print("\n🔍 Validating main root agent...")

    try:
        from smallbizpal.agent import root_agent

        print("  ✅ Root agent imported successfully")
        print(f"     - Name: {root_agent.name}")
        print(f"     - Model: {root_agent.model}")
        print(
            f"     - Sub-agents: {len(root_agent.sub_agents) if root_agent.sub_agents else 0}"
        )

        if root_agent.sub_agents:
            for i, sub_agent in enumerate(root_agent.sub_agents):
                print(f"       {i+1}. {sub_agent.name}")

        return True

    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return False


def main():
    """Main validation function."""
    print("🚀 SmallBizPal Configuration Validation")
    print("=" * 50)

    all_valid = True

    # Validate global config
    if not validate_global_config():
        all_valid = False

    # Validate individual agents
    agents_to_validate = [
        ("Business Discovery", "smallbizpal.agents.business_discovery"),
        ("Orchestrator", "smallbizpal.agents.orchestrator"),
    ]

    for agent_name, module_path in agents_to_validate:
        if not validate_agent_config(agent_name, module_path):
            all_valid = False

    # Validate main agent
    if not validate_main_agent():
        all_valid = False

    print("\n" + "=" * 50)
    if all_valid:
        print("🎉 All configurations are valid!")
        print("\nNext steps:")
        print("1. Set your GOOGLE_API_KEY environment variable")
        print("2. Run: adk web smallbizpal/agent.py")
        print("3. Test your agents in the web interface")
    else:
        print("❌ Some configurations have issues. Please fix them before proceeding.")
        sys.exit(1)


if __name__ == "__main__":
    main()
