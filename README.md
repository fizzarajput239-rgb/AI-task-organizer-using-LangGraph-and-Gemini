# AI Task Organizer (LangGraph + Gemini)

Turns a casual message into an organized, prioritized to-do list.

## Workflow
START -> Task Extraction -> Task Prioritization -> Format Results -> END

## Setup
1. `python -m venv venv` and activate it
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your Gemini API key
   (get one at https://aistudio.google.com/apikey)
4. `python main.py`

## Structure
- `main.py`        : terminal entry point
- `src/config.py`  : API key + Gemini model
- `src/state.py`   : shared graph state
- `src/schemas.py` : structured output schemas
- `src/nodes.py`   : the 3 nodes
- `src/graph.py`   : LangGraph workflow wiring
