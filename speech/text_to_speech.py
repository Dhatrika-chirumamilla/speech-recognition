import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import os
import datetime
import pyperclip
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen for voice commands
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        try:
            # Adjust for ambient noise to improve recognition accuracy
            recognizer.adjust_for_ambient_noise(source)
            # Listen for the first phrase
            audio = recognizer.listen(source, timeout=5)
            # Recognize speech using Google Web API
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.WaitTimeoutError:
            speak("No command detected.")
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")
        return ""




def google_search():
    speak("What would you like to search on Google?")
    query = listen_command()
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching Google for {query}.")
    else:
        speak("No search query provided.")

def find_location():
    speak("What location should I find on Google Maps?")
    location = listen_command()
    if location:
        webbrowser.open(f"https://www.google.com/maps/place/{location}")
        speak(f"Finding location {location} on Google Maps.")
    else:
        speak("No location provided.")

def file_navigation():
    speak("Which directory should I open?")
    directory = listen_command()
    if directory:
        try:
            os.startfile(directory)
            speak(f"Opening directory {directory}.")
        except FileNotFoundError:
            speak("Directory not found. Please try again.")
    else:
        speak("No directory provided.")

def current_date_time():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    speak(f"The current date and time is {date_time}.")
    print(f"Current date and time: {date_time}")

def copy_text():
    speak("What text should I copy?")
    text = listen_command()
    if text:
        pyperclip.copy(text)
        speak(f"Text copied: {text}")
    else:
        speak("No text provided.")

def paste_text():
    text = pyperclip.paste()
    if text:
        pyautogui.write(text)
        speak("Text pasted.")
    else:
        speak("Clipboard is empty.")

def exit_program():
    speak("Exiting the program. Goodbye!")
    sys.exit()

# Main loop
def main():
    speak("Voice-controlled virtual assistant activated.")
    while True:
        command = listen_command()

       
        if "google search" in command:
            google_search()
        elif "find location" in command:
            find_location()
        elif "file navigation" in command:
            file_navigation()
        elif "current date and time" in command:
            current_date_time()
        elif "copy" in command:
            copy_text()
        elif "paste" in command:
            paste_text()
        elif "exit" in command:
            exit_program()
        else:
            speak("Command not recognized. Please try again.")

if __name__ == "__main__":
    main()
