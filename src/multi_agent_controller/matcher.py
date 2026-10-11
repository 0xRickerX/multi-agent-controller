def skill_match(agent, capability):
    return 1.0 if capability in agent.skills else 0.20


def score_agent(agent, capability, weights):
    return (
        skill_match(agent, capability) * weights["skill_match"]
        + agent.reputation * weights["reputation"]
        + agent.availability * weights["availability"]
        + agent.cost_efficiency * weights["cost_efficiency"]
    )
