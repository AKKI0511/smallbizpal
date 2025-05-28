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

import logging
import os
from pathlib import Path


def setup_logging(log_level: str = "INFO", log_file: str = None) -> logging.Logger:
    """Set up logging configuration for SmallBizPal.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path

    Returns:
        Configured logger instance
    """
    # Create logs directory if logging to file
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

    # Configure logging format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Set up basic configuration
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        filename=log_file,
        filemode="a" if log_file else None,
    )

    # Also log to console if logging to file
    if log_file:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, log_level.upper()))
        console_formatter = logging.Formatter(log_format)
        console_handler.setFormatter(console_formatter)

        logger = logging.getLogger("smallbizpal")
        logger.addHandler(console_handler)
    else:
        logger = logging.getLogger("smallbizpal")

    return logger


# Default logger instance
logger = setup_logging(
    log_level=os.getenv("ADK_LOG_LEVEL", "INFO"), log_file=os.getenv("LOG_FILE", None)
)
