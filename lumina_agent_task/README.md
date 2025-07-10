# 🧠 LangGraph Non-Linear Agent (Mistral + Ollama)

## 📌 Project Description

This project demonstrates a non-linear agent system built using **LangGraph**, powered by the **Mistral 7B** model running locally via **Ollama**. It dynamically routes inputs to appropriate handlers like summarizer, math solver, translator, or time reporter, all orchestrated through a graph of nodes.

## ⚙️ Tech Stack

- **LangGraph** - Node-based orchestration for LLMs
- **LangChain** - LLM integration layer
- **Ollama** - Run open-source LLMs locally
- **Mistral 7B** - Lightweight reasoning model
- **Python 3.10+**

## 🚀 Features

- 🔁 Non-linear agent flow
- 📐 Math solving
- 📝 Text summarization
- 🌐 English to Hindi translation
- ⏰ Current time reporting
- 🧠 Fallback response for unknown inputs

## 📁 Files

- `agent_graph.py` — Main agent graph code
- `README.md` — This documentation
- `how_to_run.txt` — Step-by-step usage guide

## ✅ Test Examples

- `"summarize: LangGraph is a powerful orchestration tool."`
- `"34 + 12 / 2"`
- `"translate: Hello, how are you?"`
- `"What is the current time?"`
- `"Tell me something about the ocean."`

## 🔗 References

- [LangGraph Documentation](https://python.langchain.com/docs/langgraph/)
- [Ollama Setup](https://ollama.com/)
- [Mistral 7B Model](https://ollama.com/library/mistral)
