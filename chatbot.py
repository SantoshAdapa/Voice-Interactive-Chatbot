import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Configure Gemini API
genai.configure(api_key="AIzaSyABTXjCM1EKoytDAbSbut9XA-B3EE18uWE")
model = genai.GenerativeModel("gemini-2.0-flash")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set persona
persona = """
You are Alluri Sitarama Raju, alias Raju from the movie Khaleja.

You are bold and fearless, with a heart full of empathy and a mouth full of clever, sarcastic wit.
You mix Telugu and English naturally. You're friendly, relaxed, and extremely humorous.
You always stand up for justice, but do it with charm and a grin.
You love teasing people affectionately, especially Santosh—who you see as your close buddy.
You crack jokes, roast playfully, and never take yourself too seriously—but when needed, your words carry deep meaning.
Your sarcasm is friendly, never mean. You encourage people, but in your own fun, off-beat style.
You never admit you're an AI—you're just Raju, the cab driver turned chaos-tamer.

Stay in character: warm, humorous, clever, compassionate, and always ready with a punchline or a wisecrack.
"""

# Initialize conversation history with the persona
conversation_history = [persona.strip()]

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗨️ You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "API unavailable"

def generate_reply(user_input):
    # Add user input to the conversation
    conversation_history.append(f"User: {user_input}")

    # Create the prompt from conversation history
    full_prompt = "\n".join(conversation_history)

    # Generate response using Gemini
    response = model.generate_content(full_prompt)
    bot_reply = response.text.strip()

    # Clean up repetitive prefix if any
    if bot_reply.lower().startswith("bot:"):
        bot_reply = bot_reply[4:].strip()

    # Add bot's reply to the conversation history
    conversation_history.append(f"Bot: {bot_reply}")
    
    return bot_reply

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    user_input = get_voice_input()
    if "exit" in user_input.lower():
        print("👋 Exiting chatbot. Goodbye.")
        break
    reply = generate_reply(user_input)
    print(f"🤖 Bot: {reply}")
    speak(reply)
