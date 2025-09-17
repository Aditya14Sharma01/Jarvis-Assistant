import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import vlc
from time import sleep
import random as r
import openai
from AppOpener import open, close

# Set API key securely
import os
openai.api_key = os.getenv("OPENAI_API_KEY")  # Load API key from environment variable

print("hello")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again, please...")
        return "None"
    return query.lower()

def ask_gpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are JARVIS, a virtual AI assistant."},
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "I'm unable to process your request right now."

def play_video(file_path):
    vlc_instance = vlc.Instance()
    media_player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(file_path)
    media_player.set_media(media)
    media_player.play()
    media_player.set_fullscreen(True)

    while media_player.get_state() != vlc.State.Ended:
        sleep(0.1)

    media_player.stop()
    media_player.release()

def wishMe():
    speak("Initial checks completed.")
    speak("Backing up configurations.")
    speak("Databases initialized.")
    speak(f"Establishing connection to satellite {r.randint(10,99)}")
    speak("System is online.")

    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning, sir.")
    elif hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")

    speak(r.choice(["How can I assist you today?", "What's the plan for today?", "Ready to tackle the day's tasks!"]))

if __name__ == "__main__":
    play_video("startup.mp4")  # Play intro video
    wishMe()

    while True:
        query = takeCommand()

        if "goodbye" in query or "shut down" in query:
            speak(r.choice(["Shutting down. Goodbye!", "System going offline.", "Powering off."]))
            break

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any matching results.")

        elif "time" in query:
            speak(f"Sir, the time is {datetime.datetime.now().strftime('%H:%M:%S')}")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "sleep mode" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "date" in query:
            speak(f"Today's date is {datetime.date.today()}")

        elif "open " in query:
            app_name = query.replace("open ", "").strip()
            open(app_name, match_closest=True)
            speak(f"Opening {app_name}")

        elif "close " in query:
            app_name = query.replace("close ", "").strip()
            close(app_name, match_closest=True)
            speak(f"Closing {app_name}")

        else:
            response = ask_gpt(query)
            speak(response)
