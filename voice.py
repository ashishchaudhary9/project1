import google as google
import pyttsx3          #pyttsx3 is a text-to-speech conversion library.    (class pyttsx3 import engine)
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')    #Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
voices=engine.getProperty('voices')    # nss- for mac-os-x and epeak- on every other platform.

print(voices[0].id)                            #getProperty gets the current value of an engine property
engine.setProperty('voice',voices[0].id)    #voices[0] for male and voice[1] for female


def speak (audio):         #jo audio milegi use ye pronounce kregi.
    engine.say(audio)
    engine.runAndWait()     #Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately. Returns when all commands queued before this call are emptied from the queue.


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('i am shaktiman , please tell me how may i help you')

def takeCommand():
    # it takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1       # seconds of non-speaking audio before a phrase is considered complete #ye bolne ke baad rukega k ab tum bolo vrna ye complete ho jayega
        audio=r.listen(source)

    try:
        print('recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print("user said :",{query})       # f string is used here \n is for new line

    except Exception as e:
        #print(e)

        print('say it again please...')
        return 'None'
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aashishchaudhary9@gmail.com','write your password')
    server.sendmail('aashishchaudhary9@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()   #ye takeCommand ko lower case string me change kr dega
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open(youtube.com)

        elif 'open google' in query:
            webbrowser.open(google.com)

        elif 'open stackoverflow' in query:
            webbrowser.open(stackoverflow.com)

        elif 'play music' in query:
            music_dir= 'D:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak('sir ,the time is',strTime)

        elif 'open code' in query:
            codepath='C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1.1\\bin\\pycharm64.exe'
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to='aashishchaudhary9@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('sorry,couldn\'t send the email')

