from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import requests, base64, json
from PIL import Image
from io import BytesIO
import numpy as np
import cv2

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyBtktLHb_GFBOFGii2ccBWSh-Y4-SSf42w")  
model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_text(text):
    try:
        prompt = f"""
        You are a fact-checking AI. Analyze the following text/article for credibility:

        "{text}"

        Tasks:
        1. Assign a credibility score (0–100).
        2. Classify as one of: Real, Fake, Misleading, Uncertain, or Humor/Meme.
        3. Explain WHY in a structured way:
           - Evidence (or lack of it)
           - Sources (are any cited? are they credible?)
           - Tone (neutral, sensational, conspiratorial, etc.)
           - Factual Reliability (consistent with known facts or not)
           - Extraordinary Claims (unsupported or backed up)
        4. Keep explanation concise but detailed enough to justify the score.
        """

        response = model.generate_content(prompt)
        analysis = response.text.strip()

        
        credibility_score = 60
        label = "Uncertain"

       
        if "real" in analysis.lower():
            credibility_score = 80
            label = "Real"
        elif "fake" in analysis.lower():
            credibility_score = 20
            label = "Fake"
        elif "misleading" in analysis.lower():
            credibility_score = 40
            label = "Misleading"
        elif "humor" in analysis.lower() or "meme" in analysis.lower():
            credibility_score = 90
            label = "Humor/Meme"

        return {
            "credibility_score": credibility_score,
            "text_label": label,
            "text_explanation": analysis
        }

    except Exception as e:
        return {
            "credibility_score": None,
            "text_label": "Error",
            "text_explanation": f"Text analysis failed: {str(e)}"
        }



@app.route("/analyze", methods=["POST"])
def analyze_post():
    try:
        data = request.json
        text = data.get("text", "")

        result = {}

       
        if text:
            text_result = analyze_text(text)
            result.update(text_result)
        else:
            result.update({
                "credibility_score": None,
                "text_label": "No Text",
                "text_explanation": "No text was provided for analysis."
            })

        return jsonify(result)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

