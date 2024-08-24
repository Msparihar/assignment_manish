import os
from openai import OpenAI
from dotenv import load_dotenv
import base64
import requests

load_dotenv(override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_input(prompt, data, image=None):
    """Handles input and routes to appropriate LLM response generator."""
    if image:
        return generate_llm_response_image(prompt, image)
    else:
        return generate_llm_response_text(prompt, data)

def generate_llm_response_text(prompt, data):
    """Generates LLM response for text input."""
    messages = [
        {"role": "system", "content": "You are a helpful assistant that analyzes various types of data, including text documents, images, and pandas DataFrames."},
        {"role": "user", "content": f"{prompt}\n\nData: {data}\n\nPlease specify the input type for accurate analysis."}
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

def generate_llm_response_image(prompt, image):
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
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
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

    return response.json()['choices'][0]['message']['content'].strip()