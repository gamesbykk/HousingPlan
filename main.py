import streamlit as st
import requests
import io
from PIL import Image

# API configuration
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit app layout
st.title("Housing Plan Generator")
st.write("Generate custom housing plans by specifying rooms and layout features.")

# User input for the description of the housing plan
plan_description = st.text_input("Describe your housing plan (e.g., '1 kitchen, 1 bedroom'):")

# Generate button
if st.button("Generate Plan"):
    if plan_description:
        # Query the model
        image_bytes = query({"inputs": plan_description})
        
        # Display the generated image
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Generated Housing Plan")
    else:
        st.warning("Please enter a description for the housing plan.")

