from src.multi_agent_controller import MultiAgentController, TaskRequest


def test_returns_verified_run():
    controller = MultiAgentController()
    result = controller.run(TaskRequest(goal="Research AI infra and write a report"))
    assert result.status == "VERIFIED"
    assert len(result.crew) > 0


def test_has_execution_steps():
    controller = MultiAgentController()
    result = controller.run(TaskRequest(goal="Build a product launch strategy"))
    assert "PLAN" in result.steps
    assert "VERIFY" in result.steps
    assert "DELIVER" in result.steps
