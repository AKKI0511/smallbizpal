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

from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def store_report(markdown_content: str, report_date: str) -> Dict[str, Any]:
    """Store a markdown report in the reports directory.

    Args:
        markdown_content: The generated markdown report content
        report_date: Date of the report in YYYY-MM-DD format

    Returns:
        Dictionary with storage status and file path information
    """
    try:
        # Validate inputs
        if not markdown_content or not markdown_content.strip():
            return {
                "success": False,
                "error": "Markdown content cannot be empty",
                "file_path": None,
            }

        if not report_date:
            return {
                "success": False,
                "error": "Report date is required",
                "file_path": None,
            }

        # Validate date format
        try:
            datetime.strptime(report_date, "%Y-%m-%d")
        except ValueError:
            return {
                "success": False,
                "error": f"Invalid date format: {report_date}. Use YYYY-MM-DD format.",
                "file_path": None,
            }

        # Create reports directory if it doesn't exist
        reports_dir = Path("data/reports")
        reports_dir.mkdir(parents=True, exist_ok=True)

        # Generate filename
        filename = f"{report_date}_report.md"
        file_path = reports_dir / filename

        # Add generation timestamp to the report
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        report_with_timestamp = (
            f"{markdown_content.strip()}\n\n---\n*Report generated on {timestamp}*\n"
        )

        # Write the report to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(report_with_timestamp)

        return {
            "success": True,
            "file_path": str(file_path),
            "filename": filename,
            "message": f"Report successfully saved to {file_path}",
            "size_bytes": len(report_with_timestamp.encode("utf-8")),
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to store report: {str(e)}",
            "file_path": None,
        }
