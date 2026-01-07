import speech_recognition as sr
import pyttsx3
import datetime
import os

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    speak(f"{greeting}. I am your personal assistant.")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            return ""

def execute_command(command):

    #  Current Time
    if "time" in command:
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%I:%M:%S %p')}")
        return

    #  Current Date
    if "date" in command:
        today = datetime.datetime.now()
        speak(f"Today's date is {today.strftime('%A, %d %B %Y')}")
        return

    #  SEARCH 
    if command.startswith("search"):
        search_query = command.replace("search", "").strip()
        if search_query:
            speak(f"Searching for {search_query}")
            os.system(f'cmd /c start https://www.google.com/search?q={search_query.replace(" ", "+")}')
        else:
            speak("What should I search?")
        return

    #  Open Google
    if "open google" in command:
        os.system("cmd /c start https://www.google.com")
        speak("Opening Google")
        return

    #  Open YouTube
    if "open youtube" in command:
        os.system("cmd /c start https://www.youtube.com")
        speak("Opening YouTube")
        return

    # Open Notepad
    if "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")
        return

    #  Exit
    if "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    speak("Sorry, I didn't understand")

#  Start Assistant
wish_user()

while True:
    command = listen()
    if command:
        execute_command(command)
