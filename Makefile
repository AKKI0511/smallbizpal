.PHONY: help install check fix test lint format type-check coverage clean

help: ## Show this help message
	@echo "SmallBizPal Development Commands:"
	@echo ""
	@echo "  make check     - Run all checks (same as CI)"
	@echo "  make fix       - Fix all formatting and linting issues"
	@echo "  make test      - Run tests with coverage"
	@echo "  make install   - Install dependencies"
	@echo "  make clean     - Clean cache and temp files"
	@echo ""

install: ## Install dependencies using uv
	uv sync --group dev

check: ## Run all checks (EXACTLY matches CI pipeline)
	@echo "Running all checks..."
	uv run flake8 smallbizpal/ --count --select=E9,F63,F7,F82 --show-source --statistics
	uv run flake8 smallbizpal/ --count --exit-zero --max-complexity=10 --max-line-length=327 --statistics
	uv run black --check smallbizpal/ tests/
	uv run isort --check-only smallbizpal/ tests/
	uv run mypy smallbizpal/
	uv run pytest tests/ --cov=smallbizpal --cov-report=xml --cov-report=term-missing

fix: ## Fix formatting and linting issues automatically
	@echo "Fixing formatting and linting issues..."
	uv run black smallbizpal/ tests/
	uv run isort smallbizpal/ tests/

test: ## Run tests with coverage
	uv run pytest tests/ --cov=smallbizpal --cov-report=xml --cov-report=term-missing

lint: ## Run linting checks only
	uv run flake8 smallbizpal/ --count --select=E9,F63,F7,F82 --show-source --statistics
	uv run flake8 smallbizpal/ --count --exit-zero --max-complexity=10 --max-line-length=327 --statistics

format: ## Check formatting only
	uv run black --check smallbizpal/ tests/
	uv run isort --check-only smallbizpal/ tests/

type-check: ## Run type checking only
	uv run mypy smallbizpal/

coverage: ## Generate detailed coverage report
	uv run pytest tests/ --cov=smallbizpal --cov-report=html --cov-report=term-missing
	@echo "Coverage report generated in htmlcov/index.html"

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .coverage
	rm -rf htmlcov/