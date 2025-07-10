# 🧠 LangGraph Agent Assistant (Internship Task - Agent Track)

This project implements a **non-linear agent** using [LangGraph](https://github.com/langchain-ai/langgraph) and [Mistral](https://ollama.com/library/mistral) via [Ollama](https://ollama.com/), as part of the **Agent Track Internship Task**. It dynamically routes user input through different nodes — Math, Summary, Translator, or Fallback — using a graph-based architecture.

## 🚀 Features

- Interactive CLI assistant with a dynamic menu
- Non-linear agent graph with conditional routing
- Powered by **LangGraph + LangChain + Ollama + Mistral 7B**
- Includes: 
  - 📌 Summary
  - ➗ Math Solver
  - 🌐 Translator (to Hindi)
  - 🤷‍♂️ Fallback for random/general queries

## 🛠️ Tech Stack

- Python 3.10+
- LangGraph
- LangChain
- Ollama (Mistral model)
- Terminal (CLI)

## 📦 Installation & Setup

1. **Clone the repo** (or copy the code into `agent_graph.py`):
   ```bash
   git clone <your-repo-url>
   cd <project-folder>
   ```

2. **Set up virtual environment (optional but recommended)**:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install langgraph langchain langchain-community
   ```

4. **Install and start Ollama with Mistral**:
   ```bash
   # Download Ollama (if not already)
   https://ollama.com/download

   # Pull the Mistral model
   ollama pull mistral
   ```

5. **Run the app**:
   ```bash
   python agent_graph.py
   ```

## 🧪 Example Interaction

```
🤖 Welcome to the LangGraph Agent Assistant!

🔘 Please choose an option:
1. Summary
2. Math
3. Translator
4. Fallback
5. Exit

Enter your choice (1-5): 1
📝 Enter your input: summarize: LangGraph helps structure workflows using nodes.

✅ Final Output: LangGraph simplifies AI orchestration using a graph-based approach...
```

## 📁 Files

- `agent_graph.py`: Main application file containing LangGraph node logic and CLI
- `README.md`: This file (usage instructions, setup guide)

## ✅ Completed Task Checklist

- [x] LangGraph Agent with multiple functional nodes
- [x] Math, Summary, Translator, Fallback nodes
- [x] Conditional routing based on input
- [x] Dynamic CLI interface
- [x] Submission-ready, clean and modular code

## 🙌 Credits

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://python.langchain.com/)
- [Ollama](https://ollama.com/)
- [Mistral 7B](https://ollama.com/library/mistral)

