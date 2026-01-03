import pyttsx3

def tts(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    # Set properties (optional)
    engine.setProperty('rate', 175)    # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
    # Convert text to speech
    print(text)
    engine.say(text)
    engine.runAndWait()

# Example usage
# text_to_speech("Hello, this is a text-to-speech conversion.")
