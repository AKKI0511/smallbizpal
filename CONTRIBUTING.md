# Contributing to SmallBizPal

We welcome contributions to SmallBizPal! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Google API Key for Gemini models ([Get one here](https://aistudio.google.com/app/apikey))

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/AKKI0511/smallbizpal.git
   cd smallbizpal
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   # Windows CMD
   .venv\Scripts\activate.bat
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   uv pip install -e .
   uv pip install pytest pytest-asyncio pytest-cov black isort flake8 mypy pre-commit
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your Google API key
   ```

## 🛠️ Development Workflow

### Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

Run all checks:
```bash
# Format code
black smallbizpal/ tests/
isort smallbizpal/ tests/

# Lint code
flake8 smallbizpal/ tests/

# Type check
mypy smallbizpal/
```

### Testing

We use pytest for testing. All new features should include tests.

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=smallbizpal --cov-report=html

# Run specific test file
pytest tests/test_specific.py

# Run tests for specific agent
pytest tests/unit/test_business_discovery/
```

### ADK Evaluation

For agent-specific changes, run ADK evaluations:

```bash
# Run evaluation on specific agent
adk eval smallbizpal/ evaluation/datasets/business_discovery_accuracy.evalset.json

# Run all evaluations
python scripts/run_evaluation.py
```

## 📝 Contribution Guidelines

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests and checks**
   ```bash
   pytest
   black smallbizpal/ tests/
   isort smallbizpal/ tests/
   flake8 smallbizpal/ tests/
   mypy smallbizpal/
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add business discovery agent
fix: resolve customer engagement timeout issue
docs: update API documentation
test: add unit tests for marketing generator
```

### Code Review Guidelines

- **Be respectful**: Provide constructive feedback
- **Be specific**: Point to specific lines and suggest improvements
- **Test thoroughly**: Ensure changes work as expected
- **Consider performance**: Evaluate impact on agent response times
- **Check ADK compliance**: Ensure changes follow ADK best practices

## 🏗️ Architecture Guidelines

### Agent Development

When creating new agents:

1. **Follow ADK patterns**: Use `LlmAgent` or `Agent` classes
2. **Implement proper error handling**: Handle API failures gracefully
3. **Add comprehensive tests**: Unit tests and integration tests
4. **Create evaluation datasets**: For measuring agent performance
5. **Document agent capabilities**: Clear descriptions and examples

### Multi-Agent Coordination

- Use the orchestrator pattern for agent coordination
- Implement proper message passing between agents
- Handle agent failures and fallbacks
- Maintain agent state consistency

### Tool Integration

- Follow ADK tool conventions
- Add proper error handling for external APIs
- Include rate limiting and retry logic
- Document tool capabilities and limitations

## 🐛 Bug Reports

When reporting bugs, please include:

- **Environment details**: OS, Python version, ADK version
- **Steps to reproduce**: Clear, minimal reproduction steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Error messages**: Full error traces
- **Agent logs**: Relevant ADK logs

## 💡 Feature Requests

For new features:

- **Use case description**: Why is this needed?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches evaluated
- **ADK compatibility**: How does it fit with ADK patterns?

## 📚 Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions and classes
- Update API documentation
- Include examples for new features
- Update evaluation datasets as needed

## 🤝 Community

- Be welcoming to newcomers
- Help others learn ADK and agent development
- Share knowledge and best practices
- Participate in discussions and reviews

## 📄 License

By contributing to SmallBizPal, you agree that your contributions will be licensed under the Apache 2.0 License.

---

Thank you for contributing to SmallBizPal! 🎉 