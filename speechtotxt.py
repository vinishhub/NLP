#spech to text
import speech_recognition as sr
filename=r"C:\Users\Student\AppData\Local\Programs\Python\Python37-32\male.wav"
r=sr.Recognizer()
with sr.AudioFile(filename)as source:
    audio_data=r.record(source)
    text=r.recognize_google(audio_data)
    print(text)
