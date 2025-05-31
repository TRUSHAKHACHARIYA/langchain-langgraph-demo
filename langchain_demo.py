# langchain_demo.py

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def langchain_simple_demo():
    # Define your prompt template
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="Write a short description about {topic}."
    )

    # Initialize the OpenAI LLM (make sure OPENAI_API_KEY is set in your environment)
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    # Create a LangChain chain with the prompt and LLM
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain with input
    topic = "LangChain"
    result = chain.run(topic)

    print("LangChain Output:")
    print(result)

if __name__ == "__main__":
    langchain_simple_demo()
