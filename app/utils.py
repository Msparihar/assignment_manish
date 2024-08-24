import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("UNSTRUCTURED_API_KEY")
api_url = os.getenv("UNSTRUCTURED_API_URL")

def load_data(file):
    """Load and parse data from various file types."""
    if file.type == "text/plain":
        return handle_text(file)
    elif file.type.startswith("image/"):
        return None, None  # Image files are handled separately
    elif file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return parse_with_unstructured(file)
    elif file.type == "application/pdf":
        return parse_with_unstructured(file)
    else:
        raise ValueError("Unsupported file type")

def handle_text(file):
    """Handle plain text files."""
    return file.getvalue().decode('utf-8'), None

def parse_with_unstructured(file):
    """Parse Excel and PDF files using the Unstructured API."""
    response = requests.post(
        api_url,
        headers={
            "accept": "application/json",
            "unstructured-api-key": api_key,
        },
        files={"files": file}
    )
    
    if response.status_code != 200:
        raise Exception(f"Failed to parse the file: {response.status_code} - {response.text}")
    
    data = response.json()
    # Combine all text elements from the parsed data
    all_text = "\n".join(item.get("text", "") for item in data)

    return all_text, data
