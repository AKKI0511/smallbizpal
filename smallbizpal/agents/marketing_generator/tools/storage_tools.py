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

import uuid
from datetime import UTC, datetime
from typing import Any, Dict, Optional

from google.adk.tools import ToolContext

from smallbizpal.shared.services import knowledge_base_service


def store_marketing_asset(
    content: str,
    content_type: str,
    tool_context: ToolContext,
    platform: str = "universal",
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Store a marketing asset in the knowledge base.

    Args:
        content: The generated marketing content (text)
        content_type: Type of content (slogan, social_post, ad_copy, blog_outline)
        tool_context: The context of the tool.
        platform: Target platform (instagram, linkedin, facebook, twitter, universal)
        metadata: Additional metadata including hashtags, tone, target_audience, etc.

    Returns:
        Dictionary with storage status and asset information
    """
    try:
        user_id = tool_context._invocation_context.session.user_id

        if not content or not content.strip():
            return {
                "success": False,
                "error": "Content cannot be empty",
                "asset_id": None,
            }

        if not content_type:
            return {
                "success": False,
                "error": "Content type is required",
                "asset_id": None,
            }

        # Generate unique asset ID
        asset_id = f"{content_type}_{platform}_{uuid.uuid4().hex[:8]}"

        # Prepare asset data
        asset_data = {
            "id": asset_id,
            "content": content.strip(),
            "content_type": content_type,
            "platform": platform,
            "created_at": datetime.now(),
            "metadata": metadata or {},
            "status": "active",
            "version": "1.0",
        }

        # Add content analysis metadata
        asset_data["metadata"].update(
            {
                "character_count": len(content),
                "word_count": len(content.split()),
                "has_hashtags": "#" in content,
            }
        )

        # Validate platform-specific requirements
        validation_result = _validate_content_for_platform(
            content, platform, content_type
        )
        if not validation_result["valid"]:
            asset_data["metadata"]["validation_warnings"] = validation_result[  # type: ignore
                "warnings"
            ]

        # Store in knowledge base
        knowledge_base_service.store_marketing_asset(user_id, asset_data)

        return {
            "success": True,
            "asset_id": asset_id,
            "message": f"Successfully stored {content_type} for {platform}",
            "validation": validation_result,
            "metadata": asset_data["metadata"],
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to store marketing asset: {str(e)}",
            "asset_id": None,
        }


def list_marketing_assets(
    tool_context: ToolContext,
    content_type: Optional[str] = None,
    platform: Optional[str] = None,
    include_metadata: bool = True,
) -> Dict[str, Any]:
    """Retrieve marketing assets from the knowledge base.

    Args:
        tool_context: The context of the tool.
        content_type: Filter by content type (optional)
        platform: Filter by platform (optional)
        include_metadata: Whether to include detailed metadata

    Returns:
        Dictionary with list of matching marketing assets
    """
    try:
        user_id = tool_context._invocation_context.session.user_id

        # Get all marketing assets from knowledge base
        all_assets = knowledge_base_service.get_marketing_assets(user_id)

        if not all_assets:
            return {
                "assets": [],
                "total_count": 0,
                "message": "No marketing assets found",
            }

        # Apply filters
        filtered_assets = all_assets

        if content_type:
            filtered_assets = [
                asset
                for asset in filtered_assets
                if asset.get("content_type") == content_type
            ]

        if platform:
            filtered_assets = [
                asset for asset in filtered_assets if asset.get("platform") == platform
            ]

        # Format response
        response_assets = []
        for asset in filtered_assets:
            formatted_asset = {
                "id": asset.get("id"),
                "content": asset.get("content"),
                "content_type": asset.get("content_type"),
                "platform": asset.get("platform"),
                "created_at": asset.get("created_at"),
                "status": asset.get("status", "active"),
            }

            if include_metadata:
                formatted_asset["metadata"] = asset.get("metadata", {})

            response_assets.append(formatted_asset)

        # Sort by creation date (newest first)
        response_assets.sort(key=lambda x: x.get("created_at", ""), reverse=True)

        return {
            "assets": response_assets,
            "total_count": len(response_assets),
            "filters_applied": {"content_type": content_type, "platform": platform},
            "message": f"Retrieved {len(response_assets)} marketing assets",
        }

    except Exception as e:
        return {
            "assets": [],
            "total_count": 0,
            "error": f"Failed to retrieve marketing assets: {str(e)}",
        }


def _validate_content_for_platform(
    content: str, platform: str, content_type: str
) -> Dict[str, Any]:
    """Validate content against platform-specific requirements.

    Args:
        content: The content to validate
        platform: Target platform
        content_type: Type of content

    Returns:
        Dictionary with validation results
    """
    warnings = []
    char_count = len(content)

    # Platform-specific character limits
    platform_limits = {
        "twitter": 280,
        "instagram": 2200,
        "facebook": 2000,
        "linkedin": 3000,
        "universal": 500,  # Default limit
    }

    limit = platform_limits.get(platform, platform_limits["universal"])

    if char_count > limit:
        warnings.append(
            f"Content exceeds {platform} character limit ({char_count}/{limit})"
        )

    # Content type specific validations
    if content_type == "slogan" and char_count > 50:
        warnings.append("Slogan should be under 50 characters for memorability")

    if content_type == "ad_copy" and not any(
        cta in content.lower()
        for cta in ["visit", "book", "call", "shop", "learn", "contact"]
    ):
        warnings.append("Ad copy should include a clear call-to-action")

    # Platform-specific validations
    if platform in ["instagram", "twitter"] and "#" not in content:
        warnings.append(f"{platform.title()} content typically benefits from hashtags")

    if platform == "linkedin" and content_type == "social_post":
        if not any(
            prof_word in content.lower()
            for prof_word in [
                "insight",
                "strategy",
                "professional",
                "industry",
                "expertise",
            ]
        ):
            warnings.append("LinkedIn content should emphasize professional value")

    return {
        "valid": len(warnings) == 0,
        "warnings": warnings,
        "character_count": char_count,
        "platform_limit": limit,
    }


def save_content_to_kb(
    platform: str, content: str, asset_type: str, tool_context: ToolContext
) -> str:
    """Saves a piece of marketing content to the shared knowledge base.

    Args:
        platform: The platform the content is intended for (e.g., 'Twitter', 'LinkedIn').
        content: The generated marketing content.
        asset_type: The type of marketing asset (e.g., 'Social Post', 'Email Body').
        tool_context: The context of the tool.

    Returns:
        A message indicating the content has been saved successfully.
    """
    user_id = tool_context._invocation_context.session.user_id

    asset_data = {
        "platform": platform,
        "content": content,
        "asset_type": asset_type,
        "created_at": datetime.now(UTC).isoformat(),
    }

    knowledge_base_service.store_marketing_asset(user_id, asset_data)

    return f"Content for {platform} of type '{asset_type}' saved successfully to the knowledge base."
