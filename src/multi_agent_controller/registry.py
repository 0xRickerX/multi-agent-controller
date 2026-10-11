from .models import Agent


def default_agents():
    return [
        Agent("Research Agent", ["research", "sources", "analysis"], 0.94, 0.92, 0.88),
        Agent("Coding Agent", ["code", "implementation", "debugging"], 0.93, 0.84, 0.80),
        Agent("Data Agent", ["data", "metrics", "analysis"], 0.91, 0.90, 0.86),
        Agent("Strategy Agent", ["strategy", "planning", "prioritization"], 0.92, 0.86, 0.82),
        Agent("Writing Agent", ["writing", "copy", "documentation"], 0.90, 0.95, 0.90),
        Agent("Verification Agent", ["verification", "review", "quality"], 0.96, 0.88, 0.84),
    ]
