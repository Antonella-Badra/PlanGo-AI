from flask import Flask, request, render_template
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    
    city = request.form.get('city')
    days = request.form.get('days')
    travelers = request.form.get('travelers')
    budget = request.form.get('budget')
    style = request.form.get('style')
    interests = request.form.get('interests')
    
    
    prompt = (
        f"You are a professional travel guide. Create a detailed and interesting travel itinerary for {city} "
        f"for {days} days, for {travelers} travelers. The total budget is {budget} euros. "
        f"The travel style is '{style}' and the main interests are '{interests}'. "
        f"Break down the plan day by day, suggest local places to visit, and include relevant food tips."
    )
    
    try:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt,
        )
        
        ai_response = response.text
    except Exception as e:
        ai_response = f"Error while accessing the API: {str(e)}"
    
    return render_template('index.html', result=ai_response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)