# 🎙️ Voice-Interactive-Chatbot

A Python-based chatbot that combines **Google’s Gemini AI**, **speech recognition**, and **text-to-speech** to create an engaging, voice-driven assistant.  
The chatbot also features a **Flask-powered web interface** where users can switch between multiple **personas** (Raju, Baahubali, Assistant) for a more dynamic experience.

---

## 🚀 Features
- 🎤 **Voice Input**: Speak naturally, and the bot listens with `speech_recognition`.
- 🗣️ **Voice Output**: The bot replies with `pyttsx3` text-to-speech.
- 🤖 **AI-powered Responses**: Uses `google-generativeai` (Gemini) for intelligent, contextual replies.
- 🎭 **Multiple Personas**:
  - **Raju** (from *Khaleja*) – witty, sarcastic, and fun.
  - **Baahubali** – powerful, domain-specific responses about Mahishmati.
  - **Assistant** – calm, professional, and helpful.
- 🌐 **Web Interface**: Simple Flask app with `index.html` for chatting via browser.

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Voice-Interactive-Chatbot.git
   cd Voice-Interactive-Chatbot

2. **Create and activate a virtual environment (recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Mac/Linux
    venv\Scripts\activate      # On Windows
    
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

---

## ▶️ Usage

1. **Run as a Voice Chatbot**
   ```bash
   python chatbot.py

- Speak into your microphone 🎤
- The bot replies with voice 🗣️
- Say “exit” anytime to quit.

2. **Run as a Web Application**
   ```bash
    python chatbot.py
   
- Open your browser at http://127.0.0.1:5000/
- Chat with the bot using the web UI
- Switch personas (Raju, Baahubali, Assistant)

---

## 📂 Project Structure
    website/
    ├── __pycache__/
    │   └── personas.cpython-313.pyc
    ├── static/
    │   ├── script.js
    │   ├── styles.css
    ├── templates/
        └── index.html
    ├── app.py
    ├── personas.py
    README.md
    chatbot.py
    requirements.txt
---

## ✨ Example Personas

- **Raju (Khaleja)**  
  Clever, sarcastic, mixes Telugu + English, playful roasting.  

- **Baahubali**  
  Domain-specific, answers only about Mahishmati & Baahubali.  

- **Assistant**  
  Calm, professional, task-focused helper.  

---

## 🔒 API Key Setup
This project requires a Google Gemini API key.
Replace the placeholder in `chatbot.py` with your actual key:
```python
genai.configure(api_key="YOUR_API_KEY_HERE")

