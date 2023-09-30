from dataclasses import dataclass
from typing import Union, Dict, Any


@dataclass
class ToolOutput:
    # the action input
    input: Union[str, Dict[str, Any]]
    # the observation from LLM, can be modified by callback handler
    observation: str
