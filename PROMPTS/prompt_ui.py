from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task='text-generation',max_new_tokens=50)

model = ChatHuggingFace(llm = llm)

st.header("Research Tool")

input = st.text_input("Enter your prompt")

if st.button('Summarize'):
    result = model.invoke(input)
    st.write(result.content)

st.write('First UI Developed by Aditya')