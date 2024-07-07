import pyttsx3  #Text-to-speech library
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

#Initialize the text-to-speech engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Function to speak out the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Function to greet
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Iris. How can I help you today?")

#Function to take voice input and return text
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        print("Sorry, I couldn't understand that. Can you repeat?")
        return "None"
    return query

def main():
    greet()
    while True:
        query = take_command().lower()

        if 'hello' in query:
            speak("Hello! How can I assist you?")
        elif 'introduce yourself' in query:
            speak("I am Iris. I can perform tasks such as searching Wikipedia, opening websites, playing music, and more. Feel free to ask me anything!")
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open website' in query:
            webbrowser.open("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")    #Replace this with any website    
        elif 'play music' in query:
            music_dir = 'C:\\Users\\YourUsername\\Music'    #Replce this with your music directory
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))
        elif 'what is the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")
        else:
            speak("Sorry, I didn't understand. Can you please repeat?")
        if input("Press 'q' to quit or '⏎' to continue: ").lower() == 'q':
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
