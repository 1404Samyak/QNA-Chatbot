from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

import streamlit as st 

import os
from dotenv import load_dotenv
load_dotenv()

#Langsmith tracing
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_PROJECT"]="QNA-Chatbot"
langchain_api_key=os.getenv("LANGCHAIN_API_KEY")
groq_api_key=os.getenv("GROQ_API_KEY")


#Prompt_template
prompt_template=ChatPromptTemplate.from_messages(
    [("system","You are a wonderful assistant and pls respond to the queries of the user"),("user","Question{question}")]
)


def generate_response(question):
    model=ChatGroq(model="Gemma2-9b-It")
    parser=StrOutputParser()
    chain=prompt_template|model|parser
    answer=chain.invoke({"question":question})
    return answer


st.write("Hello user,hope u are having a nice day,go ahead with your question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input)
    st.write(response)
    
else:
    st.write("Pls give us some question")

