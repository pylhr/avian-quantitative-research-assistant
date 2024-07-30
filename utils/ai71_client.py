# ai71_client.py
from ai71 import AI71

AI71_API_KEY = "api71-api-25b2a05e-5625-437e-bfb1-54cb9cd3fcad"
client = AI71(AI71_API_KEY)


def get_llm_response(model, messages):
    response = client.chat.completions.create(model=model, messages=messages)
    return response
