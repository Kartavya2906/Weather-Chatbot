from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang)
    # Save the speech to a file
    tts.save("output.mp3")
    # Play the speech file
    os.system("start output.mp3")  # For Windows; use "open" on macOS or "xdg-open" on Linux

# Example usage
# text_to_speech("Hello, this is a text-to-speech conversion using gTTS.")
