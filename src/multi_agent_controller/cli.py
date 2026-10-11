import argparse
from .controller import MultiAgentController
from .models import TaskRequest


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Controller")
    parser.add_argument("--task", required=True)
    args = parser.parse_args()

    controller = MultiAgentController()
    result = controller.run(TaskRequest(goal=args.task))

    print("task:", result.goal)
    print("\nselected crew:")
    for a in result.crew:
        print(f"  {a.agent:20s} {a.score:.3f}  | {a.subtask}")

    print("\nexecution:")
    for i, step in enumerate(result.steps, start=1):
        print(f"  {i:02d} {step.lower()}")

    print("\nstatus:", result.status)


if __name__ == "__main__":
    main()
