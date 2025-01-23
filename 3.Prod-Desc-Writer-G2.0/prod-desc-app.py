import streamlit as st
from transformers import pipeline

# Set up the LLaMA 3.2 model (using Hugging Face pipeline)
@st.cache_resource
def load_llama_model():
    return pipeline('text-generation', model='meta-llama/Llama-2-7b-hf')

# Load the model
llama_generator = load_llama_model()

# Streamlit app layout
st.title('Personalized Product Description Writer')

# Input fields for the product details
st.subheader("Enter Product Details:")
product_name = st.text_input('Product Name', '')
product_features = st.text_area('Product Features (comma separated)', '')
target_audience = st.text_input('Target Audience', '')

# Button to trigger the description generation
if st.button('Generate Description'):
    if product_name and product_features and target_audience:
        # Construct the prompt for the LLaMA model
        prompt = (f"Write a product description for a product called '{product_name}' targeting {target_audience}. "
                  f"Features include: {product_features}.")
        
        # Generate the description using LLaMA 3.2 model
        description = llama_generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
        
        # Display the generated description
        st.subheader("Generated Product Description:")
        st.write(description)
    else:
        st.warning("Please fill in all the fields.")

# Additional optional features
st.sidebar.subheader("Customize Description")
length = st.sidebar.slider('Max Length', 50, 200, 100)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Built with 🧠 by Hruday & Ollama")
