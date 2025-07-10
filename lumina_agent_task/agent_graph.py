from langgraph.graph import StateGraph
from langchain_ollama import OllamaLLM
from typing import TypedDict, Literal, Union
import datetime

# ✅ 1. Define the AgentState using TypedDict
class AgentState(TypedDict):
    input_text: str
    result: str
    next: Literal["math", "summarizer", "fallback", "translator", "time"]

# ✅ 2. Load the Mistral model using Ollama
llm = OllamaLLM(model="mistral")

# ✅ 3. Router Node: Determines the next step based on input

def router_node(state: AgentState) -> dict:
    prompt = state["input_text"].lower()
    if "summarize" in prompt:
        return {"next": "summarizer"}
    elif any(op in prompt for op in ["+", "-", "*", "/"]):
        return {"next": "math"}
    elif "translate" in prompt:
        return {"next": "translator"}
    elif "time" in prompt or "date" in prompt:
        return {"next": "time"}
    else:
        return {"next": "fallback"}

# ✅ 4. Math Node: Solves math expressions

def math_node(state: AgentState) -> AgentState:
    expr = state["input_text"]
    response = llm.invoke(f"Solve this step-by-step: {expr}")
    return {"input_text": expr, "result": response, "next": "printer"}

# ✅ 5. Summarizer Node: Summarizes the text

def summarizer_node(state: AgentState) -> AgentState:
    text = state["input_text"].replace("summarize:", "").strip()
    response = llm.invoke(f"Summarize this in 2 lines: {text}")
    return {"input_text": state["input_text"], "result": response, "next": "printer"}

# ✅ 6. Fallback Node: Handles unknown inputs

def fallback_node(state: AgentState) -> AgentState:
    response = llm.invoke(f"Respond to this general query: {state['input_text']}")
    return {"input_text": state["input_text"], "result": response, "next": "printer"}

# ✅ 7. Translator Node: Translates to Hindi (example)

def translator_node(state: AgentState) -> AgentState:
    text = state["input_text"].replace("translate:", "").strip()
    response = llm.invoke(f"Translate this to Hindi: {text}")
    return {"input_text": state["input_text"], "result": response, "next": "printer"}

# ✅ 8. Time Node: Gives current time/date

def time_node(state: AgentState) -> AgentState:
    now = datetime.datetime.now()
    formatted = now.strftime("%A, %d %B %Y at %I:%M %p")
    return {"input_text": state["input_text"], "result": f"Current time: {formatted}", "next": "printer"}

# ✅ 9. Printer Node: Final output display

def printer_node(state: AgentState) -> AgentState:
    print("\n✅ Final Output:", state["result"])
    return state

# ✅ 10. Build the LangGraph

graph = StateGraph(AgentState)

# Add all nodes
graph.add_node("router", router_node)
graph.add_node("math", math_node)
graph.add_node("summarizer", summarizer_node)
graph.add_node("fallback", fallback_node)
graph.add_node("translator", translator_node)
graph.add_node("time", time_node)
graph.add_node("printer", printer_node)

# Entry point
graph.set_entry_point("router")

# Conditional routing from router
graph.add_conditional_edges(
    "router",
    lambda x: x["next"],
    {
        "math": "math",
        "summarizer": "summarizer",
        "fallback": "fallback",
        "translator": "translator",
        "time": "time"
    }
)

# Connect all function nodes to printer
graph.add_edge("math", "printer")
graph.add_edge("summarizer", "printer")
graph.add_edge("fallback", "printer")
graph.add_edge("translator", "printer")
graph.add_edge("time", "printer")

# Compile the app
app = graph.compile()

# ✅ 11. Test Function
def test():
    print("\n--- Test: Summary ---")
    app.invoke({"input_text": "summarize: LangGraph is used for LLM orchestration."})

    print("\n--- Test: Math ---")
    app.invoke({"input_text": "34 + 12 / 2"})

    print("\n--- Test: Translator ---")
    app.invoke({"input_text": "translate: Hello, how are you?"})

    print("\n--- Test: Time ---")
    app.invoke({"input_text": "What is the current time?"})

    print("\n--- Test: Fallback ---")
    app.invoke({"input_text": "Tell me something random about dolphins."})

# Run test
if __name__ == "__main__":
    test()
