import os
import sys
import subprocess

def install(package):
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure required packages are installed
try:
    import flask
    import flask_cors
    import transformers
    import torch
    import PIL
except ImportError:
    print("Missing required packages. Installing them now...")
    install('flask')
    install('flask-cors')
    install('transformers')
    install('torch')
    install('torchvision')
    install('Pillow')

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io
import base64

app = Flask(__name__)
CORS(app)

print("="*50)
print("Loading AI Model (this may take a minute on the first run)...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
captioner_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("AI Model Loaded successfully!")
print("="*50)

@app.route('/')
def index():
    return send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html'))

@app.route('/recognize', methods=['POST'])
def recognize():
    data = request.json
    if not data or 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    try:
        image_data = data['image']
        if ',' in image_data:
            image_data = image_data.split(',')[1]

        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')

        inputs = processor(image, return_tensors="pt")
        out = captioner_model.generate(**inputs)
        text = processor.decode(out[0], skip_special_tokens=True)

        print(f"Detected: {text}")
        return jsonify({'text': text})
    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Server running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
