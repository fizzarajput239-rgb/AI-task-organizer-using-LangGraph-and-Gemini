"""Entry point: run the AI Task Organizer in the terminal."""
from src.graph import build_graph


def main():
    app = build_graph()

    print("Describe your tasks in plain language (type 'quit' to exit).")
    print('Example: "I need to finish my assignment tomorrow, buy groceries '
          'today, and prepare for my meeting next week."\n')

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit", "q"}:
            break
        if not user_input:
            continue

        result = app.invoke({"user_input": user_input})
        print("\n" + result["final_output"] + "\n")


if __name__ == "__main__":
    main()
