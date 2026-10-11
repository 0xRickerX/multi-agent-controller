from src.multi_agent_controller import MultiAgentController, TaskRequest

controller = MultiAgentController()

result = controller.run(
    TaskRequest(
        goal="Research three AI infrastructure trends and create a launch brief"
    )
)

print(result)
