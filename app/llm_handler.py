import os
from openai import OpenAI
from dotenv import load_dotenv
import base64
import requests

load_dotenv(override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_input(system_prompt, user_prompt, data=None, image=None):
    """Handles input and routes to appropriate LLM response generator."""
    if image:
        return generate_llm_response_image(system_prompt, user_prompt, image)
    else:
        return generate_llm_response_text(system_prompt, user_prompt, data)

def generate_llm_response_text(system_prompt, user_prompt, data):
    """Generates LLM response for text input."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt.format(parsed_data=data)}
    ]

    # Create chat completion using OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

def generate_llm_response_image(system_prompt, user_prompt, image):
    """Generates LLM response for image input."""
    # Read image file and encode to base64
    image_base64 = base64.b64encode(image.getvalue()).decode('utf-8')

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {client.api_key}"
    }

    # Prepare payload for OpenAI API request
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt.format(parsed_data="[Image data]")
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    # Send POST request to OpenAI API
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Error in API call: {response.status_code} - {response.text}")

    return response.json()['choices'][0]['message']['content'].strip()