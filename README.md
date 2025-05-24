# SmallBizPal 🚀

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![ADK](https://img.shields.io/badge/Built%20with-Google%20ADK-4285F4)](https://google.github.io/adk-docs/)

> **AI-Powered Small Business Assistant** - A sophisticated multi-agent system built with Google ADK to help small businesses thrive through intelligent automation.

## 🎯 Overview

SmallBizPal is an innovative AI-powered assistant designed specifically for small businesses. Built using Google's Agent Development Kit (ADK), it employs a multi-agent architecture to provide comprehensive business support across marketing, customer engagement, and performance analytics.

## ✨ Features

### 🔍 Business Discovery Agent
- Interactive business profiling through intelligent questioning
- Target audience analysis and market positioning
- Competitive landscape assessment
- Brand voice and messaging development

### 📈 Marketing Asset Generator
- Automated creation of marketing materials (slogans, ad copy, social media content)
- Content optimization for different platforms
- Brand-consistent messaging across all materials
- SEO-optimized content generation

### 💬 Customer Engagement Agent
- Intelligent customer interaction handling
- Lead qualification and scoring
- Automated follow-up sequences
- Multi-channel communication support

### 📊 Performance Reporting Agent
- Real-time business metrics tracking
- Automated report generation
- ROI analysis and insights
- Growth trend identification

## 🏗️ Architecture

SmallBizPal employs a **multi-agent orchestration pattern** where:

- **Orchestrator Agent**: Coordinates all business assistance tasks and routes requests to specialized agents
- **Specialized Agents**: Each handles a specific domain (discovery, marketing, customer engagement, reporting)
- **Shared Services**: Common utilities for knowledge management, storage, and cross-agent communication

```
SmallBizPal
├── Orchestrator Agent (Root)
├── Business Discovery Agent
├── Marketing Generator Agent
├── Customer Engagement Agent
└── Performance Reporting Agent
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- Google API Key for Gemini models ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AKKI0511/smallbizpal.git
   cd smallbizpal
   ```

2. **Set up dependencies**
   ```bash
   # Install uv: https://docs.astral.sh/uv/getting-started/installation/
   # Create virtual environment
   uv venv

   # Install dependencies
   uv sync  # or make install

   # With dev dependencies (optional)
   uv sync --group dev
   ```

3. **Configure environment**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env and add your Google API key
   # GOOGLE_API_KEY=your_gemini_api_key_here
   ```

4. **Run SmallBizPal**
   ```bash
   # Start the ADK development UI
   adk web
   
   # Or run directly in Python
   python -c "from smallbizpal.agent import root_agent; print(root_agent)"
   ```

## 🛠️ Development

### Project Structure

```
smallbizpal/
├── smallbizpal/               # Main ADK package
│   ├── agent.py              # ADK entry point (contains root_agent)
│   ├── agents/               # Multi-agent system
│   │   ├── orchestrator/     # Orchestrator agent
│   │   ├── business_discovery/ # Business discovery agent
│   │   ├── marketing_generator/ # Marketing asset generator
│   │   ├── customer_engagement/ # Customer engagement agent
│   │   └── performance_reporting/ # Performance reporting agent
│   ├── shared/               # Shared utilities and services
│   ├── config/               # Global configuration
│   └── callbacks/            # ADK callbacks and middleware
├── tests/                    # Test suite
├── evaluation/               # ADK evaluation datasets
├── docs/                     # Documentation
└── scripts/                  # Utility scripts
```

### Development Workflow

**🚀 Two Essential Commands:**

```bash
# 1. Check everything (EXACTLY matches CI)
make check

# 2. Fix formatting and linting issues
make fix
```

**📋 Complete Workflow:**

```bash
# Make your code changes...

# Fix any formatting issues automatically
make fix

# Check everything (must pass before pushing)
make check

# If check passes, you can safely push to GitHub
git add .
git commit -m "Your changes"
git push
```

**🔧 Optional: Set up pre-commit hooks for automatic checking:**

```bash
# Install pre-commit hooks
uv run pre-commit install

# Now every commit will automatically run checks
git commit -m "Your changes"  # Automatically runs all checks
```

**📚 Other useful commands:**

```bash
make help          # Show all available commands
make test          # Run tests only
make coverage      # Generate detailed coverage report
make clean         # Clean up cache files
```
### Running Tests
```bash
# Run all tests
pytest
# Run with coverage
pytest --cov=smallbizpal --cov-report=html
# Run specific test
pytest tests/unit/test_orchestrator/
```

### ADK Evaluation

```bash
# Run evaluation on specific agent
adk eval smallbizpal/ evaluation/datasets/business_discovery_accuracy.evalset.json

# Run all evaluations
python scripts/run_evaluation.py
```

## 🎮 Usage Examples

### Basic Business Consultation

```python
from smallbizpal.agent import root_agent

# Simple interaction
response = root_agent.run("I need help creating a marketing plan for my bakery")
print(response.content)
```

### Using ADK Web UI

1. Start the development UI: `adk web`
2. Navigate to `http://localhost:8000`
3. Interact with SmallBizPal through the web interface
4. View agent interactions, tool calls, and performance metrics

## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [Agent Specifications](docs/agent_specifications.md)
- [API Documentation](docs/api_documentation.md)
- [Deployment Guide](docs/deployment_guide.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
- Powered by [Gemini 2.0 Flash](https://ai.google.dev/models/gemini)
- Inspired by the needs of small business owners everywhere

## 📞 Support

- 📧 Email: [akkijoshi0511@gmail.com](mailto:akkijoshi0511@gmail.com)
- 💬 Discussions: [GitHub Discussions](https://github.com/AKKI0511/smallbizpal/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/AKKI0511/smallbizpal/issues)

---

**Happy Business Building!** 🎉
