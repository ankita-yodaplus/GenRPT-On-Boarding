from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("What is the capital of {country}?")
llm = OpenAI()
parser = StrOutputParser()

chain = prompt | llm | parser

response=chain.invoke({"country": "France"})
print(response)