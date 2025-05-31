# LangChain & LangGraph Demo Collection

This repository provides simple, illustrative demos showcasing how to use two powerful frameworks for working with Large Language Models (LLMs): **LangChain** and **LangGraph**. Both libraries help developers build applications powered by language models, but with different approaches and abstractions.

---

## About LangChain

[LangChain](https://python.langchain.com/en/latest/) is a framework designed to simplify the development of applications that integrate language models. It provides modular components like prompt templates, chains, agents, and memory, allowing you to build complex NLP workflows in a composable and scalable way.

**Key Concepts from LangChain Documentation:**

- **Prompt Templates:** Define reusable prompts with variables.
- **LLMs:** Wrap language models like OpenAI GPT.
- **Chains:** Link multiple components to create a workflow.
- **Agents:** Make decisions and perform actions based on user input.
- **Memory:** Maintain context across interactions.

**In this demo (`langchain_demo.py`), we demonstrate:**

- Creating a simple prompt template.
- Initializing an OpenAI LLM instance.
- Creating an `LLMChain` to combine prompt and LLM.
- Running the chain with an input to generate text.

For more, visit the [LangChain Quickstart Guide](https://python.langchain.com/en/latest/getting_started/quickstart.html).

---

## About LangGraph

[LangGraph](https://github.com/langgraph/langgraph) is a framework for building complex LLM workflows using a graph-based approach. Each node in the graph represents a computation step or interaction with a model. This enables modular design and visual orchestration of language tasks.

**Key Concepts from LangGraph Documentation:**

- **Graph:** Core structure holding nodes and edges.
- **Nodes:** Units of computation, like LLM completions or custom logic.
- **Edges:** Define data flow between nodes.
- **Input/Output Connections:** Define how data moves through the graph.
- **Execution:** Run the graph with inputs to get outputs.

**In this demo (`langgraph_demo.py`), we show:**

- Creating a graph instance.
- Adding an OpenAI completion node.
- Connecting graph input to the node’s prompt.
- Running the graph to generate text output.

For more, check out the [LangGraph GitHub README](https://github.com/langgraph/langgraph#readme).

---

## Setup Instructions

1. Install required libraries:

```bash
pip install langchain langgraph openai
