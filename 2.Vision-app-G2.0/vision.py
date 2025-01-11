from dotenv import load_dotenv
load_dotenv() ## Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini 2.0 model and generate text
model = genai.GenerativeModel("gemini-2.0-flash-exp")
def get_gemini_response(input, image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

## Inirializing the Streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Vision Q&A Demo")
input=st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the uploaded image")

## If submit is clicked
if submit:
    response=get_gemini_response(input, image)
    st.subheader("The response is: ")
    st.write(response)