import speech_recognition as sr
from googletrans import Translator

def speech_to_hindi_text():
    # Initialize recognizer and translator
    recognizer = sr.Recognizer()
    translator = Translator()

    with sr.Microphone(device_index=2) as source:
        print("Bolna shuru karein...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            # Record audio
            audio = recognizer.listen(source)
            print("Recording complete, ab translate kar rahe hain...")

            # Convert speech to text
            text = recognizer.recognize_google(audio, language='hi-IN')  # Hindi language code
            print(f"Aapne bola: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, samajh nahi aya. Kripya phir se bolen.")
        except sr.RequestError:
            print("Speech recognition service se sampark nahi ho paya.")

# Run the function
if __name__ == "__main__":
    result = speech_to_hindi_text()
    if result:
        print(f"Nihit Hindi Text: {result}")
