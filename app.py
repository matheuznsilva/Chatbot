from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Você é um assistente virtual.
Responda apenas em português.

Historico de conversa: {context}

Usuário: {question}
Assistente:
"""

model = OllamaLLM(model="llama3")
prompt  = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Olá, tudo bem? Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Assistente: ", result)
        context += f"\nUsuário: {user_input}\nAssistente: {result}"

if __name__ == "__main__":
    handle_conversation()