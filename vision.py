from dotenv import load_dotenv
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
        return response.text

#streamlit app

st.set_page_config(page_title="Image chatbot", page_icon=":robot_face:")
st.header("Gemini Image Chatbot")
input = st.text_input("Ask me anything", key="input")
upload_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

image=""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("submit and say about the image")
if submit:
    response = get_response(input,image)
    st.subheader("Response")
    st.write(response)
