import requests
import json

# FlowiseAI API configuration
FLOWISEAI_API_URL = "https://flowiseai.example.com/api/chat"  # Replace with your FlowiseAI API URL
FLOWISEAI_API_KEY = "your_flowiseai_api_key"  # Replace with your FlowiseAI API key

def get_flowise_response(user_input):
    headers = {
        "Authorization": f"Bearer {FLOWISEAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "input": user_input,
        "context": {}  # Add any additional context if needed
    }
    response = requests.post(FLOWISEAI_API_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}, {response.text}"
