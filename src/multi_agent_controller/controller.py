import json
from pathlib import Path

from .models import Assignment, RunResult, TaskRequest
from .planner import infer_capabilities, create_subtasks
from .registry import default_agents
from .matcher import score_agent
from .verifier import verify


class MultiAgentController:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = Path(__file__).resolve().parents[2] / "config" / "controller.json"

        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.agents = default_agents()

    def _pick_agent(self, capability):
        weights = self.config["weights"]
        candidates = [
            (agent, score_agent(agent, capability, weights))
            for agent in self.agents
        ]
        return max(candidates, key=lambda x: x[1])

    def run(self, task: TaskRequest):
        capabilities = infer_capabilities(task.goal)
        subtasks = create_subtasks(capabilities)

        assignments = []
        used_agents = set()

        for capability, subtask in zip(capabilities, subtasks):
            agent, score = self._pick_agent(capability)

            if score < self.config["controller"]["min_match_score"]:
                continue

            if agent.name in used_agents and capability != "verification":
                continue

            assignments.append(
                Assignment(subtask=subtask, agent=agent.name, score=round(score, 3))
            )
            used_agents.add(agent.name)

            if len(assignments) >= self.config["controller"]["max_agents_per_task"]:
                break

        steps = ["PLAN", "MATCH", "ASSIGN", "EXECUTE"]

        if self.config["controller"]["verification_required"]:
            steps.append("VERIFY")

        steps.append("DELIVER")

        status = "VERIFIED" if verify(assignments) else "NEEDS_REVIEW"

        return RunResult(
            goal=task.goal,
            crew=assignments,
            steps=steps,
            status=status,
        )
