from dotenv import load_dotenv
load_dotenv() ## Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini 2.0 model and generate text
model = genai.GenerativeModel("gemini-2.0-flash-exp")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

## Inirializing the Streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini 2.0 Q&A Demo")
input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

## When submit is clicked 

if submit: 
    response=get_gemini_response(input)
    st.subheader("The response is: ")
    st.write(response)