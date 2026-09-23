# VisionAssist AI — Voice Assistant for Visually Impaired

VisionAssist AI is an intelligent, voice-guided accessibility platform engineered to empower visually impaired individuals. By integrating real-time computer vision models with interactive speech controls, the application acts as a personal visual narrator and navigation companion.

---

## 🌟 Key Features

* **AI-Powered Scene Captioning:** Employs the `Salesforce/blip-image-captioning-base` deep learning model to capture live camera feeds and generate instant, natural-language visual descriptions.
* **Hands-Free Voice Interface:** Complete voice-driven controls using the Web Speech API (`SpeechRecognition` & `SpeechSynthesis`) for seamless text-to-speech audio feedback.
* **Accessible UI Design:** Engineered with high-contrast color palettes (pure black background, high-visibility yellow accents, and large readable typography) optimized for low-vision accessibility.
* **Interactive Navigation & Mapping:** Integrated Leaflet.js mapping for location tracking, spatial awareness, and navigation assistance.
* **Alert & Emergency System:** Built-in alert overlays and audio signals for real-time safety warnings and status notifications.

---

## 🛠️ Tech Stack

### Backend
* **Python 3.x**
* **Flask & Flask-CORS** (REST API & Web Server)
* **PyTorch & Hugging Face Transformers** (BLIP Vision Model)
* **Pillow (PIL)** (Image Processing)

### Frontend
* **HTML5 / CSS3 / JavaScript (ES6+)**
* **Web Speech API** (Speech Recognition & Text-to-Speech)
* **Leaflet.js** (Interactive Maps & Geolocation)

---

## 📁 Project Structure

```
Visually Impaired APP/
├── app.py          # Flask backend server & AI model inference pipeline
├── index.html       # Web UI, camera stream, speech engine & maps
├── README.md        # Project documentation
└── .gitignore       # Git exclusion rules
```

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure Python 3.8+ is installed on your system.

### 2. Clone Repository
```bash
git clone https://github.com/Prasannadp46/VisionAssist-AI-Voice-Assistant-for-Visually-Impaired.git
cd VisionAssist-AI-Voice-Assistant-for-Visually-Impaired
```

### 3. Install Dependencies
Dependencies (`flask`, `flask-cors`, `transformers`, `torch`, `torchvision`, `Pillow`) will be automatically checked and installed on first run, or you can manually install them:
```bash
pip install flask flask-cors transformers torch torchvision Pillow
```

### 4. Run Application
```bash
python app.py
```
> **Note:** On the first execution, the app will download the pre-trained Salesforce BLIP vision model (~900MB).

### 5. Access Application
Open your browser and navigate to:
```
http://localhost:5000
```

---

## 📡 API Endpoints

### `GET /`
Serves the main accessible web dashboard (`index.html`).

### `POST /recognize`
Processes base64-encoded camera frames and returns textual scene descriptions.

* **Request Body:**
  ```json
  {
    "image": "data:image/jpeg;base64,..."
  }
  ```
* **Response:**
  ```json
  {
    "text": "a person holding a white cup in a brightly lit kitchen"
  }
  ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the repository issues page.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
