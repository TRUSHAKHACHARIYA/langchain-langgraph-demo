# langgraph_demo.py

from langgraph.graph import Graph
from langgraph.nodes.llm_node import OpenAICompletionNode

def langgraph_simple_demo():
    # Create a graph instance
    graph = Graph()

    # Create an OpenAI completion node
    llm_node = OpenAICompletionNode(
        name="openai_completion",
        model="gpt-3.5-turbo",
        temperature=0.7
    )

    # Add the node to the graph
    graph.add_node(llm_node)

    # Connect graph input to the node's prompt
    graph.connect_input_to_node("topic", llm_node, "prompt")

    # Define graph input data
    inputs = {
        "topic": "LangGraph"
    }

    # Run the graph with inputs
    output = graph.run(inputs)

    print("LangGraph Output:")
    print(output[llm_node.name])

if __name__ == "__main__":
    langgraph_simple_demo()
