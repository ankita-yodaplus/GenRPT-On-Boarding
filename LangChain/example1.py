import os
from dotenv import load_dotenv
from  langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework

st.title('Celebrity Search results')  
input_text = st.text_input("Search the topic you want")

# Prompt Templates

first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template='Tell me about celebrity {name}'
)

# OpenAI LLMS
llm=OpenAI(temperature=0.8)

output_parser = StrOutputParser()

chain = first_input_prompt | llm | output_parser


if input_text:
    st.write(chain.invoke(input_text))   