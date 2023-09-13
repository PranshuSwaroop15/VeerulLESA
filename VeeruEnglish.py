import pyttsx3

import datetime

import speech_recognition as sr

import smtplib
import wolframalpha

from secret import senderemail,epwd,to

from email.message import EmailMessage

import pyautogui

import webbrowser as wb # use the following link : 'https://web.whatsapp.com/send?phone='+phone_no+ '&text='+Message

from time import sleep

import wikipedia

import pywhatkit

import requests

# http://api.openweathermap.org/data/2.5/weather?q=ghaziabad&units=imperial&appid=63bf49b4945d4f66ae57242fc62a209e


from  newsapi import NewsApiClient

import clipboard

import os

import pyjokes 
 
import time as tt

import string

import random

import psutil

from nltk.tokenize import word_tokenize

from newvoices import speak

from gtts import gTTS
from langdetect import detect
import openai

import speech_recognition as sr

openai.api_key = "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"




# engine=pyttsx3.init() 

# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
 
# def speak(audio):
#     engine.say(audio)

#     engine.runAndWait()  

# def getvoices(voice):

#     voices=engine.getProperty('voices')

#     # print(voices[1].id)

#     if voice==1:
#         engine.setProperty('voice',voices[1].id)

#         speak("Hello Sir, this is Alfred your buttler!")
#     if voice==2:

#         engine.setProperty('voice',voices[2].id)

#         speak("Hello Sir, this is Dory")

def time():

    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is ")
    speak(Time)


def date():
    date=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)

    year=int(datetime.datetime.now().year)

    speak("Today's date is ")
    speak(date)
    speak(month)
    speak(year)

def greetings():

    hour=datetime.datetime.now().hour

    if hour>=4 and hour<12:
        speak("Good Morning Master Bruce!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Master Bruce!")

    elif hour>=18 and hour<22:
        speak("Good Evening Master Bruce!")

    else:
        speak("Good Night Master Bruce")

def wishme():

    greetings()
    speak("Its been a long time ,  Welcome back Sir, How Can I help you?")
    # date()
    # time()
    

# while True:

#     voice=int(input("Enter the voice id : "))
#     getvoices(voice)

# wishme()
# date()
# time()

def takecommandCmd():

    query=input("How can I help you Sir?\n")

    return query

def takeCommandMic():

    r=sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio=r.listen(source)

    try:

        print("Recognizing...")

        query=r.recognize_google(audio,language="en-IN")

        print(query)
    
    except Exception as e:

        print(e)

        speak("Sorry,I couldn't understand Please say it again")

        return "None"
    return query


def sendEmail(receiver,subject,content):

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail,epwd)

    # server.sendmail(senderemail,to,content)

    email=EmailMessage()

    email['From']=senderemail
    email['To']=receiver
    email['Subject']=subject

    email.set_content(content)

    server.send_message(email)
    
    server.close()

def sendWhatsapp(phone_no,message):
    
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+ '&text='+Message)
    sleep(15)
    pyautogui.press('enter')


def searchGoogle():

    speak("Connected Sir,What should I search")

    search=takeCommandMic()

    wb.open('https://www.google.com/search?q='+search)




def news():

    newspi=NewsApiClient(api_key='660a5f3617a84eb9bddf0d8a577b0779')

    speak("What topic you need to hear the news about ")

    topic=takeCommandMic()

    data=newspi.get_top_headlines(q=topic,language='en'
                                  ,page_size=5)


    newsdata=data['articles']


    for x,y in enumerate(newsdata):

        print(f"{x},{y['description']}")

        speak(f"{x},{y['description']}")



    speak(f"This is it for now, I will update you later")


def text2speech():
    text=clipboard.paste()

    print(text)

    speak(text)
    #
def screenshot():
 
    name_img=tt.time()

    name_img='D:\AI Assistant Alfred\screenshot\{name_img}.png'

    img=pyautogui.screenshot(name_img)
    speak("The screenshot has been taken")
    img.show()


def passgen():

    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.ascii_letters
    s4=string.punctuation


    passlen=8

    s=[]

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)

    newpass=("".join(s[0:passlen]))

    
    print(newpass)
    speak("A new password has been generated ")


def cpu():

    usage=str(psutil.cpu_percent())

    speak("Speak CPU Usage"+ usage)

    battery=psutil.sensors_battery()

    speak("And the battery usage is")

    speak(battery.percent)


def wolframe():
    # H8UPE5-7WX9XPRHYE

    question = speak("Please ask a question")
  
    # App id obtained by the above steps
    app_id = "H8UPE5-7WX9XPRHYE"
    
    # Instance of wolf ram alpha 
    # client class
    client = wolframalpha.Client(app_id)
   
    ques=takeCommandMic()

    # Stores the response from 
    # wolf ram alpha
    res = client.query(ques)
    
    # Includes only text from the response
    answer = next(res.results).text
    
    speak(answer)

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



# sendEmail()
if __name__ == "__main__":

    # i=input("Whom do you want to speak\n")

    # if i=="Alfred":
    

    #     getvoices(1)
    #     wishme()

    # elif i=="Dory":

    #     getvoices(2)

    #     wishme()

    

    speak("Hello, This is your Virtual Assistant Veeru,What can I help you?")

    wakeword="veeru"
   

    while True:
        query=takeCommandMic().lower()

        query1=query
        query=word_tokenize(query)
        print(query)
        if wakeword in query:

            if 'date' in query:

                date()

            elif 'time' in query:

                time()

            elif 'email'  in query:

                email_list={
                    "Pranshu":"pranshuswaroop4@gmail.com"
                    }

                
                try:

                    speak("To whom should I send")

                    name=takeCommandMic()

                    receiver=email_list[name]

                    speak("What should be the subject")

                    subject=takeCommandMic()

                    speak("What Should I send?")

                    content=takeCommandMic()

                    sendEmail(receiver,subject,content)

                    speak("The email has been sent")
                
                except Exception as e:
                    print(e)
                    speak("I missed it, Can you say that again?")



            elif 'message' in query:

                user_names={
                    'Pranshu':"+91 8826 7378 30",

                    'Suyash':"+91 9810 8140 56",

                    'Mummy':"+91 9599 2633 87",

                    'Rishabh':"+91 9717 4382 30"

                    }
                
                try:

                    speak("To whom should I send")

                    name=takeCommandMic()

                

                    phone_no = user_names[name]

                    
                    speak("What Should I send?")

                    content=takeCommandMic()

                    sendWhatsapp(phone_no,content)


                    speak("The Message has been sent")
                
                except Exception as e:
                    print(e)
                    speak("I missed it, Can you say that again?")


            elif 'wikipedia' in query:

                speak("Searching on wikipedia")

                query=takeCommandMic()
                query=query.replace('search',"")
                

                result=wikipedia.summary(query, sentences = 3) 

                print(result) 

                speak(result)

            elif 'google' in query:

                searchGoogle() 

            elif 'youtube' in query:

                speak("What should I play on Youtube")

                

                play=takeCommandMic()
                play=play.replace('play',"")
                

                speak(f"Playing {play} on Youtube")
                pywhatkit.playonyt(play)

            elif 'weather' in query:

                url="http://api.openweathermap.org/data/2.5/weather?q=ghaziabad&units=imperial&appid=63bf49b4945d4f66ae57242fc62a209e"

                res=requests.get(url)
                

                data=res.json()

                weather=data['weather'][0]['main']

                temp=data['main']['temp']
                
                desc=data['weather'][0]['description']


                humidity=data['main']['humidity']
                
                tempcelsuis=round( (temp-32) * 5/9 )

                cityname=data['name']
                
                country=data['sys']['country']


                visibility=data['visibility']


                print(cityname)
                print(weather)

                print(tempcelsuis)

                print(desc)

                speak(f"The temperature in {cityname} is {tempcelsuis} degree celsuis")
                speak(f"The weather is with {weather}")
                speak(f"there are {desc} in the sky")
                
                if(humidity>50):
                    speak(f"Humidity is {humidity} which means that the humidity is quite high and the visibility is {visibility} meter")
                
                else:
                    speak(f"Humidity is {humidity} which means that the humidity is ideal and the visibility is {visibility} meter")
        

            


            elif 'news' in query:
                news()
                
            elif "read" in query:

                text2speech()

            elif 'open application' in query:

                codepath= 'C:\Program Files\Mozilla Firefox\\firefox.exe'

                os.startfile(codepath)

            elif 'open' in query:

                os.system('explorer C://{}'.format(query.replace('Open','')))


            elif 'joke' in query:

                speak(pyjokes.get_joke())

            elif 'screenshot' in query:

                screenshot()

            elif 'remember' in query:

                speak("what do you want me to remember")

                data=takeCommandMic()

                data=data.replace("remember","")

                speak("I have remembered that"+data)

                remember=open('data.txt','w')

                remember.write(data)

                remember.close()

            elif "recall" in query:

                remember=open('data.txt','r')

                
                speak("You told me to remember"+remember.read())

            elif "generate a password" in query:

                passgen()

            elif "usage" in query:

                cpu()
            
            elif "mathematics" in query:

                wolframe()
            elif 'offline' in query:

                speak("Have a Good Day Sir")

                quit()

            else:
                generate(query1)



