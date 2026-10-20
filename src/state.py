"""Shared state passed between LangGraph nodes."""
from typing import List, TypedDict


class State(TypedDict, total=False):
    user_input: str
    tasks: List[dict]
    prioritized_tasks: List[dict]
    final_output: str
