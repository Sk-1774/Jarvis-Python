import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')   #get audio voices
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis. How may i help you?")

def takeCmd():
    #It takes mic input from user and returns a string as output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speak("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        speak("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Please repeat the command...")
        speak("Please repeat the command...")
        return "None"
    return query


#def sendEmail(to, content):


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCmd().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            #webbrowser.open("youtube.com")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new("youtube.com")

        elif 'open google' in query:
            #webbrowser.open("google.com")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new("google.com")

        elif 'open codechef' in query:
            #webbrowser.open("codechef.com")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new("codechef.com")

        elif 'open canva' in query:
            #webbrowser.open("canva.com")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new("canva.com")

        elif 'open netflix' in query:
            #webbrowser.open("netflix.com")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new("netflix.com")


        elif 'play music' in query:
            music_dir = "E:\\Songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

        elif 'open spotify' in query:
            spotifyPath = "C:\\Users\\Admin\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath) 

        # elif 'email to sk' in query:
        #     try:
        #         speak("what shoould be the content?")
        #         content = takeCmd()
        #         to= "sanhitak17@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry email could not be sent!")

        elif 'hi jarvis' in query:
            speak("hi")
            #query.sleep(500)
            speak("S K")
            #speak("k")


        elif 'thank you' in query:
            speak("you're welcome")

        elif 'joke' in query:
            s=open("E:\\Jarvis\\Jokes.txt","r")
            m=s.readlines()
            l=[]
            for i in range(0,len(m)-1):
                x=m[i]
                z=len(x)
                a=x[:z-1]
                l.append(a)
            l.append(m[i+1])
            o=random.choice(l)
            print(o)
            speak(f"{o} hahaha")

            s.close()

        elif 'stop' in query:
            speak("Bye Bye")
            break