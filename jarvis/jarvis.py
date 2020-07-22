import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('Hi, I am jarvis your friend Gunjan. How may i help you?')

def takeCommand():
    # it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'user said: {query}')
    except Exception as e:
        # print(e)
        print('Say that again please!')
        return 'None'
    return query

# must enable less secure apps from the gmail account from which you are sending mail
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('emailaccount','password')
    server.sendmail('emailaccount',to,content)
    server.close()

if __name__ == "__main__":
    # speak("Gunjan is intelligent and smart and i am her jarvis")
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()
        # logic for ececuting tast based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia: ')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)
            # randon_song = random.randint(len(songs))
            os.startfile(os.path.join(music_dir,songs[0]))
            # os.startfile(os.path.join(music_dir,randon_song))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')

        elif 'open code' in query:
            codePath = "C:\\Users\\divya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'send email to divya' in query:
            try:
                speak('What should i say? ')
                content = takeCommand()
                to = 'emailaccount of recepent goes here'
                sendEmail(to,content)
                speak('Email has been sent! ')
            except Exception as e:
                print(e)
                speak('Sorry, can\'t send email')

        elif 'quit' in query:
            exit()


