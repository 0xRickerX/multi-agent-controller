from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    name: str
    skills: List[str]
    reputation: float
    availability: float
    cost_efficiency: float


@dataclass
class TaskRequest:
    goal: str


@dataclass
class Assignment:
    subtask: str
    agent: str
    score: float


@dataclass
class RunResult:
    goal: str
    crew: List[Assignment] = field(default_factory=list)
    steps: List[str] = field(default_factory=list)
    status: str = "PENDING"
