import pyttsx3
import os
import openai

import speech_recognition as sr

openai.api_key = "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"

start = "Your are a AI Search Engine, answer the following query with a witty answer and include validated facts only."

def generate(prompt):
    start_sequence = "{}.{}".format(start,prompt)
    completions = openai.Completion.create(
      model="text-davinci-003",
      prompt=start_sequence,
      temperature=0.1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0.51,
      presence_penalty=0.5,
      #stream = False,
      #echo = True
    )

    message = completions.choices[0].text
    # print(f"AI Response : {message}")
    # return message

    speak(message)

    print(message)

engine=pyttsx3.init() 

def speak(text):
    print("AI Response : ")
    engine.say(text)

    engine.runAndWait()  

def takeCommandMic():

    r=sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio=r.listen(source)

    try:

        print("Recognizing...")

        query=r.recognize_google(audio,language="en-IN")

        print("Human Said : "+query)
    
    except Exception as e:

        print(e)

        speak("Sorry,I couldn't understand Please say it again")

        return "None"
    return query

while True:
    
    query=takeCommandMic()

    generate(query)