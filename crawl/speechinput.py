import speech_recognition as sr
import speechoutpyttsx
def voicein():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source 
    # listening the speech and store in audio_text variable
    # print(sr.Microphone.list_microphone_names())

    with sr.Microphone() as source:
        print("Speak:")
        audio_text = r.listen(source)
        print("Thanks for your input!!!")
        # recoginze_() method will throw a request
        # error if the API is unreachable,
        # hence using exception handling
        
        
            # using google speech recognition
        try:
            print("Text: "+r.recognize_google(audio_text))
        except:
            speechoutpyttsx.tts("Sorry, I did not get that")
            # print()
            return (voicein())
    return r.recognize_google(audio_text)   
# print(voicein())