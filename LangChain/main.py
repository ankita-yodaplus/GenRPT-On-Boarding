# integrate our code with OpenAI API
import os
from dotenv import load_dotenv
from  langchain_openai import OpenAI

import streamlit as st 

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework 

st.title('Langchain Demo with OpenAI API')  
input_text = st.text_input("Search the topic you want")

# OpenAI LLMS
llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))   

