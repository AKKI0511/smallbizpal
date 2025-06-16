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

from google.adk.agents import LlmAgent

from .config import (
    PERFORMANCE_REPORTING_CONFIG,
)
from .tools import collect_metrics, store_report

performance_reporting_agent = LlmAgent(
    name=PERFORMANCE_REPORTING_CONFIG["name"],
    model=PERFORMANCE_REPORTING_CONFIG["model"],
    description=PERFORMANCE_REPORTING_CONFIG["description"],
    instruction=PERFORMANCE_REPORTING_CONFIG["instruction"].format(
        date=datetime.now().strftime("%Y-%m-%d")
    ),
    tools=[collect_metrics, store_report],
    output_key="performance_report",
)

# root_agent = performance_reporting_agent
