from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
from personas import personas

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key="AIzaSyABTXjCM1EKoytDAbSbut9XA-B3EE18uWE")
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=["POST"])
def chat():
    data = request.json
    user_input = data['user_input']
    persona_key = data['persona']

    if persona_key not in personas:
        return jsonify({"reply": "Unknown persona selected."})

    persona_text = personas[persona_key]
    prompt = f"{persona_text.strip()}\nUser: {user_input}\nBot:"
    response = model.generate_content(prompt)
    reply = response.text.strip()

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
