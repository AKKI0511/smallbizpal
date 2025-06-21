import os
from pathlib import Path
from typing import List, Dict, Any

import uvicorn
from fastapi import HTTPException
from google.adk.cli.fast_api import get_fast_api_app

# Import the knowledge base service
from smallbizpal.shared.services.knowledge_base import knowledge_base_service

# Get the directory where main.py is located
AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Example session DB URL (e.g., SQLite)
SESSION_DB_URL = "sqlite:///./sessions.db"
# Example allowed origins for CORS
ALLOWED_ORIGINS = ["http://localhost", "http://localhost:8080", "*"]
# Set web=True if you intend to serve a web interface, False otherwise
SERVE_WEB_INTERFACE = True

# Call the function to get the FastAPI app instance
# Smallbizpal deploy
app = get_fast_api_app(
    agents_dir=AGENT_DIR,
    session_service_uri=SESSION_DB_URL,
    allow_origins=ALLOWED_ORIGINS,
    web=SERVE_WEB_INTERFACE,
)

# API Routes for accessing stored data

@app.get("/api/marketing-content/{user_id}")
async def get_marketing_content(user_id: str) -> Dict[str, Any]:
    """Get all marketing content for a specific user."""
    try:
        marketing_assets = knowledge_base_service.get_marketing_assets(user_id)
        return {
            "user_id": user_id,
            "marketing_assets": marketing_assets,
            "count": len(marketing_assets)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving marketing content: {str(e)}")

@app.get("/api/reports/{user_id}")
async def get_reports(user_id: str) -> Dict[str, Any]:
    """Get all reports for a specific user."""
    try:
        reports_dir = Path("data") / user_id / "reports"
        reports = []
        
        if reports_dir.exists():
            for report_file in reports_dir.glob("*.md"):
                try:
                    with open(report_file, "r", encoding="utf-8") as f:
                        content = f.read()
                    reports.append({
                        "filename": report_file.name,
                        "content": content,
                        "created_date": report_file.name.split("_")[0] if "_" in report_file.name else "unknown",
                    })
                except Exception as e:
                    # Skip files that can't be read
                    continue
        
        return {
            "user_id": user_id,
            "reports": reports,
            "count": len(reports)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving reports: {str(e)}")

@app.get("/api/customer-engagement/{user_id}")
async def get_customer_engagement(user_id: str) -> Dict[str, Any]:
    """Get all customer interactions and engagement data for a specific user."""
    try:
        customer_interactions = knowledge_base_service.get_customer_interactions(user_id)
        performance_data = knowledge_base_service.get_performance_data(user_id)
        
        return {
            "user_id": user_id,
            "customer_interactions": customer_interactions,
            "performance_data": performance_data,
            "interactions_count": len(customer_interactions),
            "metrics_count": len(performance_data) if isinstance(performance_data, dict) else 0
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving customer engagement data: {str(e)}")

@app.get("/api/business-profile/{user_id}")
async def get_business_profile(user_id: str) -> Dict[str, Any]:
    """Get business profile data for a specific user (admin access only)."""
    try:
        # Get the business profile using the knowledge base service
        business_profile = knowledge_base_service.get_business_profile(user_id)
        profile_summary = knowledge_base_service.get_profile_summary(user_id)
        
        if business_profile is None:
            return {
                "user_id": user_id,
                "profile_exists": False,
                "business_data": {},
                "summary": profile_summary,
                "message": "No business profile found for this user"
            }
        
        # Get sanitized business data (removes sensitive fields if any)
        business_data = business_profile.get_all_data()
        
        return {
            "user_id": user_id,
            "profile_exists": True,
            "business_data": business_data,
            "summary": profile_summary,
            "last_updated": business_profile.updated_at.isoformat() if business_profile.updated_at else None,
            "total_updates": business_profile.total_updates,
            "total_fields": len(business_data)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving business profile: {str(e)}")

# You can add more FastAPI routes or configurations below if needed
# Example:
# @app.get("/hello")
# async def read_root():
#     return {"Hello": "World"}

if __name__ == "__main__":
    # Use the PORT environment variable provided by Cloud Run, defaulting to 8080
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))