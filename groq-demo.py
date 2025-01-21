from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key = "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",
    temperature=0,
)

# -----------------------------Realtime Chatting---------------------------
# messages = [
#     SystemMessage(content="You are a helpful AI assistant"),
# ]

# while(True):
#     query = input("USER: ")
#     if query == "exit":
#         break
#     messages.append(HumanMessage(content=query))
#     response = llm.invoke(messages)
#     messages.append(AIMessage(content=response.content))
#     print(f"AI: {response.content}")

# print(messages)

# ------------------------------PROMPT TEMPLATES-----------------------------
# template = "Tell me a joke about {topic}."
# prompt_template = ChatPromptTemplate.from_template(template)
# prompt = prompt_template.invoke({"topic":"cats"})
# print(prompt)
# response = llm.invoke(prompt)
# print(response.content)


# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}"),
#     ("human", "Tell me {count} jokes"), 
# ]
# promp_template = ChatPromptTemplate.from_messages(messages)
# prompt = promp_template.invoke({"count":3, "topic" : "engineering"})
# # print(prompt)
# response = llm.invoke(prompt)
# print(response.content)


# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}"),
#     HumanMessage(content="Tell me 2 jokes"),
#     # HumanMessage(content="Tell me {count} jokes")  #Wont work because the variable "count" is not replaced
# ]
# promp_template = ChatPromptTemplate.from_messages(messages)
# prompt = promp_template.invoke({"topic" : "romantic"})
# print(prompt)
# response = llm.invoke(prompt)
# print(response.content)

# ------------------------------CHAINING-----------------------------

# prompt_template = ChatPromptTemplate.from_messages([
#     ("system", "you are a great comedian who tells jokes about {topic}"),
#     ("human", "tell me {joke_count} jokes")
# ])

# chain = prompt_template | llm | StrOutputParser()

# response = chain.invoke({"topic": "Computer Engineers", "joke_count" : 3})
# print(response)

