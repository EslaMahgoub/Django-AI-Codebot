import os
from openai import OpenAI

import helpers
OPENAI_API_KEY = helpers.config("OPENAI_API_KEY", default=None, cast=str)

def get_openai_client():
    return OpenAI(
        base_url = 'http://localhost:11434/v1',
        api_key= OPENAI_API_KEY
    )   

def chat_with_openai(message, model="llama2", raw=False):
    client = get_openai_client()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "you are an amazing assistant",
            },
            {
                "role": "user",
                "content": f"{message}",
            }
        ],
    )
    if raw:
        return response
    else:
        return response.choices[0].message.content