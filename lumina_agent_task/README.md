# 🧠 LangGraph + Mistral Agentic Workflow

This project demonstrates a **non-linear agent workflow** using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://www.langchain.com/), and the open-source **Mistral 7B** model via [Ollama](https://ollama.com/).

### ✅ Features
- Modular graph-based agent system using LangGraph.
- Dynamic routing logic (router node).
- 3 functional nodes: `summarizer`, `math`, `fallback`.
- Final output handler node (`printer`).
- Works with local LLMs using Ollama and Mistral.

---

## 📦 Folder Structure

```
lumina_agent_task/
│
├── agent_graph.py         # Main LangGraph agent implementation
├── README.md              # Project overview and instructions
└── how_to_run.txt         # Simplified step-by-step run guide
```

---

## 🔧 Requirements

- Python 3.10+
- [Ollama](https://ollama.com/download)
- Mistral model installed in Ollama
- Virtual Environment (Recommended)

---

## ⚙️ Setup Instructions

```bash
# 1. Clone/download the code
cd lumina_agent_task

# 2. Create virtual environment
python -m venv langgraph_env
langgraph_env\Scripts\activate        # For Windows

# 3. Install dependencies
pip install langgraph langchain langchain-community langchain-ollama

# 4. Install Ollama and pull mistral model
# Install: https://ollama.com/download
ollama pull mistral
ollama run mistral                      # Start Ollama server
```

---

## 🚀 Running the Agent

```bash
# Make sure you're in the virtual environment
langgraph_env\Scripts\activate

# Run the agent script
python agent_graph.py
```

Expected output will include:
- Summary output from Mistral
- Math solving
- Fallback response for unknown prompts

---

## ✅ Example Inputs

```
summarize: LangGraph is used for LLM orchestration.
34 + 12 / 2
tell me something interesting
```

---

## 🙌 Credits
- LangGraph by LangChain
- Mistral model via Ollama
