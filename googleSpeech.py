import speech_recognition as sr

r=sr.Recognizer()

with sr.AudioFile("on.flac") as source:
    print("Speak")

    try:
       audio=r.listen(source)
    
       text=r.recognize_google(audio)
       print(text)
    except:
        print("Sorry not catch what you have told !!!!")