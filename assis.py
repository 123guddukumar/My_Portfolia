import requests
import speech_recognition as sr
from gtts import gTTS
import os

# API Key
LLAMA_API_KEY = "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"
LLAMA_ENDPOINT = "https://api.llama.ai/chat"

# Function to capture user voice and convert to text
def get_user_input():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening for your query in Hindi...")
        audio = recognizer.listen(source)

    try:
        # Use Google Speech-to-Text to transcribe audio
        user_text = recognizer.recognize_google(audio, language="hi-IN")
        print(f"User said: {user_text}")
        return user_text
    except Exception as e:
        print("Error in understanding audio:", str(e))
        return None

# Function to send text to LLAMA API
def query_llama_api(user_text):
    headers = {"Authorization": f"Bearer {LLAMA_API_KEY}"}
    data = {"input": user_text, "language": "hi"}  # LLAMA API assumes Hindi input
    response = requests.post(LLAMA_ENDPOINT, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get("output", "कोई उत्तर उपलब्ध नहीं है।")
    else:
        print("Error from LLAMA API:", response.status_code)
        return "कोई उत्तर उपलब्ध नहीं है।"

# Function to convert text response to speech
def speak_response(response_text):
    tts = gTTS(response_text, lang="hi")
    tts.save("response.mp3")
    os.system("start response.mp3")  # For Windows; use `afplay` for macOS or `play` for Linux

# Main Function
def main():
    user_input = get_user_input()
    if user_input:
        llama_response = query_llama_api(user_input)
        print(f"LLAMA response: {llama_response}")
        speak_response(llama_response)

if __name__ == "__main__":
    main()
