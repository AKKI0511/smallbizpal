# SmallBizPal Configuration System

This directory contains the **global configuration system** for SmallBizPal. Individual agents manage their own configuration using local `config.py` files.

## Configuration Philosophy

We follow a **decentralized configuration approach** where:

1. **Each agent folder has its own `config.py`** - Contains all agent-specific settings
2. **Global config provides shared utilities** - Application settings, model configs, and business constants
3. **Template available for consistency** - Use `agent_config_template.py` for new agents

## Global Configuration Structure

```
smallbizpal/config/
├── __init__.py                  # Main exports and utilities
├── settings.py                  # Application-wide settings (API keys, ports, etc.)
├── models.py                    # Global model configurations and utilities
├── constants.py                 # Business domain constants
├── agent_config_template.py     # Template for new agents
└── README.md                    # This file
```

## Global Config Contents

### `settings.py` - Application Settings
- API keys and authentication
- Application metadata (name, version)
- Storage and data directory settings
- ADK configuration (ports, timeouts)
- Environment-specific settings

### `models.py` - Model Configurations
- Available models in the system
- Default model selection
- Model parameter configurations (creative, analytical, precise)
- Model utility functions

### `constants.py` - Business Domain Constants
- Agent types (for categorization)
- Business categories and industries
- Marketing channels and customer segments
- Performance metrics and KPIs

## Agent-Specific Configuration

Each agent manages its own complete configuration:

```
smallbizpal/agents/your_agent/
├── config.py                    # Complete agent configuration
├── agent.py                     # Agent implementation
├── tools/                       # Agent-specific tools
└── __init__.py                  # Agent exports
```

## Creating a New Agent

1. **Copy the template**:
   ```bash
   cp smallbizpal/config/agent_config_template.py smallbizpal/agents/your_agent/config.py
   ```

2. **Customize the config**:
   - Update `AGENT_NAME`, `MODEL_NAME`, `DESCRIPTION`
   - Modify `INSTRUCTION` with your agent's system prompt
   - Configure `TOOLS_CONFIG` for your agent's tools
   - Adjust `BEHAVIOR_CONFIG` and other sections as needed

3. **Use config in your agent**:
   ```python
   from google.adk.agents import LlmAgent
   from .config import AGENT_NAME, MODEL_NAME, INSTRUCTION, DESCRIPTION, TOOLS_CONFIG
   from .tools import your_tools
   
   # Build tools based on config
   tools = []
   for tool_name, tool_config in TOOLS_CONFIG.items():
       if tool_config.get("enabled", True):
           tools.append(your_tools[tool_name])
   
   your_agent = LlmAgent(
       name=AGENT_NAME,
       model=MODEL_NAME,
       instruction=INSTRUCTION,
       description=DESCRIPTION,
       tools=tools
   )
   ```

## Using Global Configuration

Import global settings when needed:

```python
# Application settings
from smallbizpal.config import GOOGLE_API_KEY, APP_NAME, DEBUG

# Model configurations
from smallbizpal.config import DEFAULT_MODEL, get_model_config

# Business constants
from smallbizpal.config import BUSINESS_CATEGORIES, MARKETING_CHANNELS
```

## Configuration Validation

Always validate configurations after changes:

```bash
python smallbizpal/scripts/validate_config.py
```

## Best Practices

1. **Agent configs are self-contained** - Each agent should be independently configurable
2. **Use global config for shared data** - Business constants, model configs, app settings
3. **Use the template** - Start with `agent_config_template.py` for consistency
4. **Environment variables** - Use global settings for environment-specific values
5. **Validate frequently** - Run validation script during development

## Examples

- **Business Discovery Agent**: `smallbizpal/agents/business_discovery/config.py`
- **Orchestrator Agent**: `smallbizpal/agents/orchestrator/config.py`
- **Template**: `smallbizpal/config/agent_config_template.py` 