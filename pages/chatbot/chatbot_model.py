from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

chat = OpenAI(temperature=0)

converstaion = ConversationChain(
    llm=chat, verbose=True, memory=ConversationBufferMemory()
)
