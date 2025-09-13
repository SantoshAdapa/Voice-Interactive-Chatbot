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
   
▶️ Usage
1. Run as a Voice Chatbot
python chatbot.py


Speak into your microphone 🎤

The bot replies with voice 🗣️

Say “exit” anytime to quit.

2. Run as a Web Application
python chatbot.py


Open your browser at http://127.0.0.1:5000/

Chat with the bot using the web UI

Switch personas (Raju, Baahubali, Assistant)

📂 Project Structure
Voice-Interactive-Chatbot/
│── chatbot.py          # Main chatbot (voice + Flask web)
│── personas.py         # Persona definitions
│── requirements.txt    # Python dependencies
│── website/
│   └── index.html      # Web interface template
└── README.md           # Project documentation

⚙️ Requirements

Your requirements.txt should include:

google-generativeai
SpeechRecognition
pyttsx3
flask


