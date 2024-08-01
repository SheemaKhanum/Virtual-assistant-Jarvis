import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="b08de5127cd7461895daab3cafcf68dc"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open hotstar" in c.lower():
        webbrowser.open("https://hotstar.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        # parse the json response
        if r.status_code==200:
            data=r.json()
        # extract the articles
        articles=data.get('articles',[])
        # speak the headlines
        for article in articles:
            speak(article['title'])
               
if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
    # Listen for the wake word"Jarvis"   
    # Obtain audio from microphone
        r=sr.Recognizer()       
        print("recognizing...")
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source,timeout=2,phrase_time_limit=1)
        try:
            word=r.recognize_google(audio)
            print(word)   
            if (word.lower()=="jarvis"):
                speak("Yah")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source,timeout=2)
                    print("processing command....")
                    command = r.recognize_google(audio)
                    processCommand(command)
                
        except Exception as e:
            print("Error; {0}".format(e))

