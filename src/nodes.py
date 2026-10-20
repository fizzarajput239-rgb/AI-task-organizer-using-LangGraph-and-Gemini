"""The three workflow nodes."""
from .config import get_llm
from .schemas import ExtractedTasks, PrioritizedTasks
from .state import State


def extract_tasks(state: State) -> State:
    """Node 1: Gemini splits the message into individual tasks."""
    llm = get_llm().with_structured_output(ExtractedTasks)
    prompt = (
        "You are a task extraction assistant.\n"
        "Read the user's message and extract every individual task.\n"
        "For each task give a short title and the deadline mentioned "
        "(use 'Not specified' if none).\n"
        "Do not invent tasks that are not in the message.\n\n"
        f"User message:\n{state['user_input']}"
    )
    result = llm.invoke(prompt)
    return {"tasks": [t.model_dump() for t in result.tasks]}


def prioritize_tasks(state: State) -> State:
    """Node 2: Gemini assigns High / Medium / Low to each task."""
    if not state.get("tasks"):
        return {"prioritized_tasks": []}

    llm = get_llm().with_structured_output(PrioritizedTasks)
    task_lines = "\n".join(
        f"- {t['title']} (deadline: {t['deadline']})" for t in state["tasks"]
    )
    prompt = (
        "You are a task prioritization assistant.\n"
        "Assign each task a priority: High, Medium, or Low.\n"
        "Base it mainly on how soon the deadline is and how important the "
        "task seems. Closer deadlines mean higher priority.\n"
        "Return ALL tasks, keep titles and deadlines unchanged, and add a "
        "one-sentence reason.\n\n"
        f"Tasks:\n{task_lines}"
    )
    result = llm.invoke(prompt)
    return {"prioritized_tasks": [t.model_dump() for t in result.tasks]}


def format_results(state: State) -> State:
    """Node 3: Build a readable to-do list (no LLM needed)."""
    tasks = state.get("prioritized_tasks", [])
    if not tasks:
        return {"final_output": "No tasks were found in your message."}

    icons = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
    lines = ["=" * 50, "        YOUR ORGANIZED TO-DO LIST", "=" * 50]

    number = 1
    for level in ("High", "Medium", "Low"):
        group = [t for t in tasks if t["priority"] == level]
        if not group:
            continue
        lines.append(f"\n{icons[level]} {level.upper()} PRIORITY")
        lines.append("-" * 50)
        for t in group:
            lines.append(f"{number}. {t['title']}")
            lines.append(f"   Deadline : {t['deadline']}")
            lines.append(f"   Why      : {t['reason']}")
            number += 1

    lines.append("\n" + "=" * 50)
    return {"final_output": "\n".join(lines)}
