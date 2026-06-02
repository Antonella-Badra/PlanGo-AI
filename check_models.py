import os
from google import genai
from dotenv import load_dotenv

# Load your API key from the .env file
load_dotenv()

try:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    print("The following models are available for your API key:")
    
    # Request the list of all models from Google
    for model in client.models.list():
        print(model.name)
        
except Exception as e:
    print(f"Something went wrong: {e}")
