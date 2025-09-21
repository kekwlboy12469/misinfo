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

def score_to_label(score):
    if score is None:
        return "N/A"
    if score >= 70:
        return "Real"
    elif score >= 40:
        return "Uncertain"
    else:
        return "Fake"


# --- Image Analysis ---
def analyze_image_url(image_url):
    try:
        resp = requests.get(image_url, timeout=5)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content))

        explanation_parts = []

        # 1. Format / metadata check
        if img.format not in ["JPEG", "PNG", "WEBP"]:
            explanation_parts.append(f"Unusual format {img.format}, possible editing.")

        # 2. EXIF metadata check
        try:
            exif = img._getexif()
            if not exif:
                explanation_parts.append("No EXIF metadata (common in AI-generated images).")
        except:
            explanation_parts.append("EXIF could not be read.")

        # 3. Size check
        if img.size[0] < 50 or img.size[1] < 50:
            return 10, "Likely Fake/Manipulated", "Image is too small to analyze reliably."

        # 4. Pixel smoothness (AI detection heuristic)
        arr = np.array(img.convert("L"))  # grayscale
        edges = np.std(arr)  # standard deviation = texture measure
        if edges < 15:
            explanation_parts.append("Very low texture variation (plasticky look, AI sign).")

        # Final decision
        if explanation_parts:
            return 40, "Suspicious / Possibly AI", "; ".join(explanation_parts)
        else:
            return 90, "Likely Real", "No obvious AI artifacts, distortions, or manipulations detected."

    except Exception as e:
        return None, "Error", f"Image analysis failed: {str(e)}"


# --- API Route ---
@app.route("/analyze", methods=["POST"])
def analyze_post():
    try:
        data = request.json
        text = data.get("text", "")
        image_url = data.get("image", None)

        result = {}

        # --- TEXT ANALYSIS ---
        if text:
            lowered = text.lower()
            credibility_score = 60

            if any(word in lowered for word in ["govt", "official", "breaking", "shocking"]):
                credibility_score = 40
                result["text_label"] = "Potentially Misleading"
                explanation = f"Text contains sensational keywords: '{text[:80]}...'"
            elif any(word in lowered for word in ["meme", "funny", "lol", "😂", "🤣"]):
                credibility_score = 90
                result["text_label"] = "Humorous Content"
                explanation = "Text looks like humor/meme, not factual claim."
            else:
                result["text_label"] = "Neutral"
                explanation = "No misinformation cues found in text."

            result["credibility_score"] = credibility_score
            result["text_explanation"] = explanation

        else:
            result["credibility_score"] = 40
            result["text_label"] = "Fake"
            result["text_explanation"] = "No text found."

        # --- IMAGE ANALYSIS ---
        if image_url:
            score, label, explanation = analyze_image_url(image_url)
            result["image_score"] = score
            result["image_label"] = label
            result["image_explanation"] = explanation
        else:
            result["image_score"] = None
            result["image_label"] = "No Image"
            result["image_explanation"] = "No image provided."

        return jsonify(result)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
