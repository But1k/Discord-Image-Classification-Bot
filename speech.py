import speech_recognition as sr
import random
import time

def play_game(levels):
    levels = {
        "easy": ["diary", "mouse", "computer"],
    
        "medium": ["programming", "algorithm", "developer"],
    
        "hard": ["neural network", "machine learning", "artificial intelligence"]

        }

def speach():
    mic = sr.Microphone()
    recog = sr.Recognizer()

    try:
        with mic as audio_file:
            recog.adjust_for_ambient_noise(audio_file, duration=0.2)
            audio = recog.listen(audio_file)
            text = recog.recognize_google(audio, language="en-EN")
            print(f'You said: {text}')
    except sr.UnknownValueError:
        print('Voice did not recognize')
    
speach()