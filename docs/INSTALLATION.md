# Installation Guide

This guide provides step-by-step instructions for setting up and running the SmallBizPal project on your local machine.

## ✅ Prerequisites

Before you begin, ensure you have the following installed on your system:

-   **Python**: Version `3.11` or higher.
-   **Git**: For cloning the repository.
-   **`uv`**: A fast Python package installer. If you don't have it, follow the official [installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## ⚙️ Environment Setup

### 1. Clone the Repository

First, clone the project repository from GitHub to your local machine:

```bash
git clone https://github.com/AKKI0511/smallbizpal.git
cd smallbizpal
```

### 2. Configure Environment Variables

The project uses a `.env` file to manage secrets, primarily the Google API key for the Gemini models.

1.  **Create the `.env` file** by copying the provided template:
    ```bash
    cp .env.example .env
    ```

2.  **Edit the `.env` file** with your favorite text editor and add your Google API key:
    ```
    # .env
    GOOGLE_API_KEY="your_gemini_api_key_here"
    ```
    You can obtain a Google API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## 📦 Step-by-Step Installation

### 1. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.

```bash
# Create a virtual environment using uv
uv venv
```

This will create a `.venv` directory in your project folder. The `uv` command will automatically use it.

### 2. Install Dependencies

Install all required Python packages using `uv`:

```bash
# Install all production dependencies
uv sync
```
This command reads the `pyproject.toml` file and installs the exact versions of the packages specified, ensuring a reproducible environment.

## ▶️ Running the Application

For business owner and customer interactions:

```bash
# Launch the admin application
adk web
# From the "Select an agent" dropdown:
# 1) select "customer_engagement" to interact as a customer
# 2) Select "smallbizpal" to interact as a business owner
```

By default, the UI will be accessible at **`http://localhost:8000`**. This provides access to the Customer Engagement Agent and all admin agents.


## 🚀 Cloud Deployment

For production deployment to Google Cloud Run follow the instructions in the [ADK Cloud Run Deployment Guide](https://google.github.io/adk-docs/deploy/cloud-run/)

- Option 1: Using ADK CLI

```bash
adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
$AGENT_PATH
```

- Option 2: Using gcloud CLI

```bash
gcloud run deploy smallbizpal \
--source . \
--region $GOOGLE_CLOUD_LOCATION \
--project $GOOGLE_CLOUD_PROJECT \
--allow-unauthenticated \
--set-env-vars="GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT,GOOGLE_CLOUD_LOCATION=$GOOGLE_CLOUD_LOCATION,GOOGLE_GENAI_USE_VERTEXAI=$GOOGLE_GENAI_USE_VERTEXAI"
```

## 🔧 Troubleshooting

| **Symptom** | **Likely Cause** | **Fix** |
|-------------|------------------|---------|
| `ImportError: No module named 'google.adk'` | ADK not installed | Run `uv sync` again |
| `API key not found` | Missing `.env` file | Copy `.env.example` to `.env` and add your key |
| `Port 8000 already in use` | Another process using port | Use `--port 8001` or kill the other process |
| Agent responses are slow | Rate limiting | Wait a few seconds between requests |
| Tests failing | Missing dev dependencies | Run `uv sync --group dev` |

## 🧪 Running Tests

To ensure that everything is working correctly, you can run the project's test suite.

### 1. Install Development Dependencies

The testing framework and other development tools are listed as optional dependencies. Install them using `uv`:
```bash
uv sync --group dev
```

### 2. Run the Test Suite

Execute the tests using `pytest`:

```bash
pytest
```

You should see all tests passing, which validates that your installation is successful and the core functionality is working as expected.

### 3. Optional: Set Up Pre-commit Hooks

For automatic code formatting and linting:

```bash
# Install pre-commit hooks
uv run pre-commit install

# Now every commit will automatically run checks
git commit -m "Your changes"  # Automatically runs formatting and linting
``` 