from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# Funtion to load Gemini Pro Vision model
model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue() # Read the image file in bytes

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("Please upload an image to proceed")
    

## Initialize our streamlit app
st.set_page_config(page_title='MultiLanguage Invoice Extraction')

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit=st.button("Tell me about the Invoice")

input_prompt="""
You are an expert in understanding invoices, 
we will upload an invoice as an image and 
you will have to answer any questions based on the uploaded invoice image.
"""

# If submit button is clicked
if submit:
    image_data=input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is: ")
    st.write(response)
