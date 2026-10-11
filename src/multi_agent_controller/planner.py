def infer_capabilities(goal: str):
    g = goal.lower()
    caps = []

    mapping = {
        "research": ["research", "sources"],
        "launch": ["strategy", "writing"],
        "strategy": ["strategy", "planning"],
        "code": ["code", "implementation"],
        "build": ["code", "implementation"],
        "data": ["data", "analysis"],
        "report": ["research", "writing"],
        "write": ["writing"],
        "copy": ["writing"],
    }

    for key, values in mapping.items():
        if key in g:
            caps.extend(values)

    if not caps:
        caps = ["planning", "research", "writing"]

    # verification is always included as a capability in this prototype
    caps.append("verification")

    return list(dict.fromkeys(caps))


def create_subtasks(capabilities):
    label_map = {
        "planning": "Plan the work",
        "strategy": "Define strategy",
        "research": "Research the task",
        "sources": "Gather sources",
        "code": "Implement solution",
        "implementation": "Build required components",
        "data": "Analyze data",
        "analysis": "Analyze findings",
        "writing": "Synthesize final output",
        "verification": "Verify result",
    }
    return [label_map.get(c, c.title()) for c in capabilities]
