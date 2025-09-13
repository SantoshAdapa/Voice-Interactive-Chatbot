const chatBox = document.getElementById("chatBox");
const textInput = document.getElementById("textInput");

function appendMessage(sender, message) {
  const msg = document.createElement("p");
  msg.textContent = `${sender}: ${message}`;
  chatBox.appendChild(msg);
}

async function sendMessage() {
  const message = textInput.value;
  const persona = document.getElementById("personaSelect").value;
  appendMessage("You", message);
  textInput.value = "";

  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_input: message, persona: persona })
  });
  
  const data = await response.json();
  appendMessage("Bot", data.reply);
  speak(data.reply);
}

function speak(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(utterance);
}

function startVoice() {
  const recognition = new webkitSpeechRecognition();
  recognition.lang = "en-IN";
  recognition.start();

function clearChat() {
    document.getElementById("chat-box").innerHTML = "";
}

  recognition.onresult = function(event) {
    const voiceText = event.results[0][0].transcript;
    textInput.value = voiceText;
    sendMessage();
  };
}
