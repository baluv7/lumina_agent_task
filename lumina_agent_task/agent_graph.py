from langgraph.graph import StateGraph
from langchain_ollama import OllamaLLM
from typing import TypedDict, Literal

# ✅ 1. Define the Agent State
class AgentState(TypedDict):
    input_text: str
    result: str
    next: Literal["math", "summarizer", "translator", "fallback"]

# ✅ 2. Load the Mistral model via Ollama
llm = OllamaLLM(model="mistral")

# ✅ 3. Router Node
def router_node(state: AgentState) -> dict:
    prompt = state["input_text"].lower()
    if "summarize" in prompt:
        return {"next": "summarizer"}
    elif any(op in prompt for op in ["+", "-", "*", "/"]):
        return {"next": "math"}
    elif "translate" in prompt:
        return {"next": "translator"}
    else:
        return {"next": "fallback"}

# ✅ 4. Math Node
def math_node(state: AgentState) -> AgentState:
    expr = state["input_text"]
    response = llm.invoke(f"Solve this step-by-step: {expr}")
    return {"input_text": expr, "result": response, "next": "printer"}

# ✅ 5. Summarizer Node
def summarizer_node(state: AgentState) -> AgentState:
    text = state["input_text"].replace("summarize:", "").strip()
    response = llm.invoke(f"Summarize this in 2 lines: {text}")
    return {"input_text": state["input_text"], "result": response, "next": "printer"}

# ✅ 6. Fallback Node
def fallback_node(state: AgentState) -> AgentState:
    response = llm.invoke(f"Respond to this general query: {state['input_text']}")
    return {"input_text": state["input_text"], "result": response, "next": "printer"}

# ✅ 7. Translator Node
def translator_node(state: AgentState) -> AgentState:
    text = state["input_text"].replace("translate:", "").strip()
    response = llm.invoke(f"Translate this to Hindi: {text}")
    return {"input_text": state["input_text"], "result": response, "next": "printer"}

# ✅ 8. Printer Node
def printer_node(state: AgentState) -> AgentState:
    print("\n✅ Final Output:", state["result"])
    return state

# ✅ 9. Build LangGraph
graph = StateGraph(AgentState)

graph.add_node("router", router_node)
graph.add_node("math", math_node)
graph.add_node("summarizer", summarizer_node)
graph.add_node("fallback", fallback_node)
graph.add_node("translator", translator_node)
graph.add_node("printer", printer_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    lambda x: x["next"],
    {
        "math": "math",
        "summarizer": "summarizer",
        "fallback": "fallback",
        "translator": "translator"
    }
)

graph.add_edge("math", "printer")
graph.add_edge("summarizer", "printer")
graph.add_edge("fallback", "printer")
graph.add_edge("translator", "printer")

app = graph.compile()

# ✅ 10. Dynamic User Interaction Loop (Updated Menu)
def run_interactive():
    print("\n🤖 Welcome to the LangGraph Agent Assistant!\n")
    while True:
        print("\n🔘 Please choose an option:")
        print("1. Summary\n2. Math\n3. Translator\n4. Fallback\n5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\n👋 Thanks for Using!")
            break

        prompt_map = {
            "1": "summarize: ",
            "2": "",
            "3": "translate: ",
            "4": ""
        }

        if choice not in prompt_map:
            print("\n❌ Invalid choice. Please try again.")
            continue

        user_input = input("\n📝 Enter your input: ").strip()
        input_text = prompt_map[choice] + user_input

        # Run the app
        app.invoke({"input_text": input_text})

# ✅ Entry Point
if __name__ == "__main__":
    run_interactive()
