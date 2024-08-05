import streamlit as st
import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

SERPER_API_KEY = st.secrets["SERPER_API_KEY"]


def get_real_time_data(query):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, data=payload)
    data = response.json()

    return data


def format_serper_response(data):
    formatted_response = []

    if "knowledgeGraph" in data:
        kg = data["knowledgeGraph"]
        formatted_response.append(f"**{kg['title']}**")
        formatted_response.append(f"Type: {kg['type']}")
        # formatted_response.append(f"Website: {kg['website']}")
        formatted_response.append(f"Description: {kg['description']}")

        attributes = kg.get("attributes", {})
        for key, value in attributes.items():
            formatted_response.append(f"{key}: {value}")

    for result in data.get("organic", []):
        formatted_response.append(f"Title: {result['title']}")
        formatted_response.append(f"Link: {result['link']}")
        formatted_response.append(f"Snippet: {result['snippet']}")

    for question in data.get("peopleAlsoAsk", []):
        formatted_response.append(f"Q: {question['question']}")
        formatted_response.append(f"A: {question['snippet']}")

    for search in data.get("relatedSearches", []):
        formatted_response.append(f"Related Search: {search['query']}")

    return "\n".join(formatted_response)


def search_result(query):
    real_time_data = get_real_time_data(query)

    formatted_data = format_serper_response(real_time_data)

    return formatted_data
