import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit UI
st.title('Celebrity Search Results')
input_text = st.text_input("Search the topic you want")

# Prompt templates
prompt1 = PromptTemplate.from_template("Tell me about celebrity {name}")
prompt2 = PromptTemplate.from_template("When was {person} born")
prompt3 = PromptTemplate.from_template("Mention 5 major events happened around {dob} in the world")

# Output parser
parser = StrOutputParser()

# Use ChatOpenAI (preferred for newer LangChain setup)
llm = ChatOpenAI(temperature=0.8)

# Memory store (basic in-memory message history)
memory_store = {}

def get_history(session_id):
    if session_id not in memory_store:
        memory_store[session_id] = ChatMessageHistory()
    return memory_store[session_id]

# Chain 1
chain1 = prompt1 | llm | parser
chain1 = RunnableWithMessageHistory(
    chain1,
    get_history,
    input_messages_key="name",
)

# Chain 2
chain2 = prompt2 | llm | parser
chain2 = RunnableWithMessageHistory(
    chain2,
    get_history,
    input_messages_key="person",
)

# Chain 3
chain3 = prompt3 | llm | parser
chain3 = RunnableWithMessageHistory(
    chain3,
    get_history,
    input_messages_key="dob",
)

# Run the chains sequentially
if input_text:
    session_id = "user-session"  # Or use a UUID
    person = chain1.invoke({"name": input_text}, config={"configurable": {"session_id": session_id}})
    dob = chain2.invoke({"person": person}, config={"configurable": {"session_id": session_id}})
    description = chain3.invoke({"dob": dob}, config={"configurable": {"session_id": session_id}})

    st.subheader("Results")
    st.write(f"**Person**: {person}")
    st.write(f"**Date of Birth**: {dob}")
    st.write(f"**Major Events Around DOB**:\n{description}")

    # Memory display (debugging)
    with st.expander("Chat History"):
        for msg in memory_store[session_id].messages:
            st.info(f"{msg.type.capitalize()}: {msg.content}")
