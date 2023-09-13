engine=pyttsx3.init() 

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
 
def speak(audio):
    engine.say(audio)

    engine.runAndWait()