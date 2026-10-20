"""LangGraph workflow: START -> extract -> prioritize -> format -> END."""
from langgraph.graph import END, START, StateGraph

from .nodes import extract_tasks, format_results, prioritize_tasks
from .state import State


def build_graph():
    graph = StateGraph(State)

    graph.add_node("extract_tasks", extract_tasks)
    graph.add_node("prioritize_tasks", prioritize_tasks)
    graph.add_node("format_results", format_results)

    graph.add_edge(START, "extract_tasks")
    graph.add_edge("extract_tasks", "prioritize_tasks")
    graph.add_edge("prioritize_tasks", "format_results")
    graph.add_edge("format_results", END)

    return graph.compile()
