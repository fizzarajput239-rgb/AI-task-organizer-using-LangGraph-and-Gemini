"""Pydantic schemas for structured Gemini output."""
from typing import List, Literal

from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str = Field(description="Short, clear description of one task")
    deadline: str = Field(
        default="Not specified",
        description="When it is due, e.g. 'today', 'tomorrow', 'next week'",
    )


class ExtractedTasks(BaseModel):
    tasks: List[Task]


class PrioritizedTask(BaseModel):
    title: str
    deadline: str
    priority: Literal["High", "Medium", "Low"]
    reason: str = Field(description="One short sentence explaining the priority")


class PrioritizedTasks(BaseModel):
    tasks: List[PrioritizedTask]
