from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai


load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("gemini-pro")
def get_response(query):
    response=model.generate_content(query)
    return response.text

#streamlit app

st.set_page_config(page_title="Chatbot", page_icon=":robot_face:", layout="wide")
st.header("Gemini Chatbot")
input = st.text_input("Ask me anything", "Type here")
submit = st.button("Submit")

if submit:
    response = get_response(input)
    st.subheader("Response")
    st.write(response)