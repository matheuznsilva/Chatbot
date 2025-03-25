from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are a virtual assistent.
You will answer only english.

conversation history: {context}

User: {question}
Assistent:
"""

model = OllamaLLM(model="llama3")
prompt  = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("hey, how are you? Type 'exit' to finish")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Assistent: ", result)
        context += f"\nUser: {user_input}\nAssistent: {result}"

if __name__ == "__main__":
    handle_conversation()