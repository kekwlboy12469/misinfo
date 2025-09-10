from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import json
import os
import re

app = Flask(__name__)
CORS(app)

# Load API key
API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBtktLHb_GFBOFGii2ccBWSh-Y4-SSf42w")
genai.configure(api_key=API_KEY)

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"""
    Analyze the credibility of this text:

    "{text}"

    Return ONLY valid JSON, no explanations outside JSON.
    Format exactly like this:
    {{
      "credibility_score": 0-100,
      "label": "Likely True/Likely False/Suspicious",
      "explanation": "2-3 short sentences explaining why"
    }}
    """

    try:
        response = model.generate_content(prompt)

        # Try parsing JSON directly
        cleaned = response.text.strip()

        # If Gemini wrapped text, extract JSON with regex
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if match:
            cleaned = match.group(0)

        result = json.loads(cleaned)
    except Exception as e:
        # fallback if parsing fails
        result = {
            "credibility_score": 50,
            "label": "Suspicious",
            "explanation": f"Defaulted because model returned unexpected output. Raw: {response.text if 'response' in locals() else str(e)}"
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

