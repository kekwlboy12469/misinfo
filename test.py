from google.cloud import aiplatform

# Initialize Vertex AI
aiplatform.init(project="hackathon-471612", location="us-central1")

# Use the GenerativeModel interface from the generative quickstart utilities
from google.cloud.aiplatform.gapic import GenAiServiceClient

client = GenAiServiceClient()
model_name = "projects/hackathon-471612/locations/us-central1/publishers/google/models/gemini-2.5-flash"

req = {
    "model": model_name,
    "contents": [{"role": "user", "parts": [{"text": "Hello Gemini! What is COVID?"}]}],
    "generation_config": {"temperature": 0.2, "max_output_tokens": 256},
}

resp = client.generate_content(request=req)
print(resp.candidates.content.parts.text)







