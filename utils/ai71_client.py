import streamlit as st
from ai71 import AI71

# from dotenv import load_dotenv
import os

# load_dotenv()


AI71_API_KEY = st.secrets["AI71_API_KEY"]
client = AI71(AI71_API_KEY)


def get_llm_response(model, messages):
    response = client.chat.completions.create(model=model, messages=messages)
    response_message = response.choices[0].message.content
    strip_response_message = response_message.rsplit("User:", 1)[0].strip()
    return strip_response_message
