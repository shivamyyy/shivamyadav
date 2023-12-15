# Import necessary libraries
import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os
import wikipedia
import webbrowser
import pywhatkit as kit
import cv2
import datetime
import requests
from translate import Translator
import random
import speedtest
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui
import time
import pyperclip
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import openai
openai.api_key = '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'

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take user command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()
    
# Function to interact with ChatGPT API
def chatGPT(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function to chat with ChatGPT
def chatWithGPT():
    speak("How can I assist you today?")
    while True:
        user_input = takeCommand()
        if 'exit' in user_input:
            speak("Goodbye! Have a great day.")
            break

        # Send user input to ChatGPT
        response = chatGPT(user_input)

        # Speak the response from ChatGPT
        speak(response)
        # Display the response in text format
        print("Assistant:", response)

# Function to open YouTube
def openYouTube():
    webbrowser.open("https://www.youtube.com")

# Function to search on YouTube
def searchYouTube(query):
    kit.playonyt(query)

# Function to open Google and search
def searchGoogle(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Function to open Paint and create different shapes
def createShapes():
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write('paint')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # Create a rectangular spiral
    distance = 300
    while distance > 0:
        pyautogui.dragRel(distance, 0, 0.1, button="left")
        distance = distance - 10
        pyautogui.dragRel(0, distance, 0.1, button="left")
        pyautogui.dragRel(-distance, 0, 0.1, button="left")
        distance = distance - 10
        pyautogui.dragRel(0, -distance, 0.1, button="left")

# Function to open Gmail and create an email
def createEmail():
    webbrowser.open("https://mail.google.com")

# Function to open Notepad and write a message
def writeNotepadMessage(message):
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(message, interval=0.1)

# Function to open WordPad and type a message
def typeWordpadMessage(message):
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write('wordpad')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(message, interval=0.1)

# Function to tell the temperature
def tellTemperature():
    try:
        city = "mumbai"
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        temperature_celsius = temperature - 273.15
        speak(f"The temperature in {city} is {temperature_celsius:.2f} degrees Celsius.")
    except Exception as e:
        speak("Sorry, I couldn't fetch the temperature at the moment.")

# Function to tell the date
def tellDate():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today's date is {current_date}")

# Function to tell the time
def tellTime():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

# Function to open Chrome
def openChrome():
    os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

# Function to open system settings
def openSettings():
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write('settings')
    time.sleep(1)
    pyautogui.press('enter')

# Function to create a folder
def createFolder(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    speak(f"The folder '{folder_name}' has been created.")

# Function to open camera and take a picture
def openCameraAndTakePicture():
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    cv2.imwrite("captured_picture.jpg", img)
    cap.release()
    cv2.destroyAllWindows()
    speak("Picture captured.")

# Function to take a screenshot
def takeScreenshot():
    speak('Tell me a name for the file')
    name = takeCommand()
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("Screenshot saved.")

# Function to translate English sentences to Hindi
def translateToHindi():
    speak("What do you want to translate to Hindi?")
    sentence_to_translate = takeCommand()
    
    translator = Translator(to_lang="hi")
    translation = translator.translate(sentence_to_translate)
    
    speak(f"The translation to Hindi is: {translation}")


# Function to play Rock, Paper, Scissors with Jarvis
def playRockPaperScissors():
    speak("Let's play Rock, Paper, Scissors. Choose rock, paper, or scissors.")
    user_choice = takeCommand().lower()
    
    choices = ['rock', 'paper', 'scissors']
    jarvis_choice = random.choice(choices)
    
    speak(f"I chose {jarvis_choice}.")

    if user_choice in choices:
        if user_choice == jarvis_choice:
            speak("It's a tie!")
        elif (
            (user_choice == 'rock' and jarvis_choice == 'scissors') or
            (user_choice == 'paper' and jarvis_choice == 'rock') or
            (user_choice == 'scissors' and jarvis_choice == 'paper')
        ):
            speak("You win!")
        else:
            speak("I win!")
    else:
        speak("Invalid choice. Please choose rock, paper, or scissors.")

# Function to check internet speed
def checkInternetSpeed():
    speak("Checking internet speed. Please wait.")
    
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # in Mbps
    upload_speed = st.upload() / 10**6  # in Mbps
    
    speak(f"My current download speed is {download_speed:.2f} Mbps, and upload speed is {upload_speed:.2f} Mbps.")

# Function to shut down the system
def shutDownSystem():
    speak("Are you sure you want to shut down the system?")
    confirmation = takeCommand().lower()
    
    if 'yes' in confirmation:
        os.system("shutdown /s /t 1")
    else:
        speak("Shutting down cancelled.")
# Function to open WhatsApp and send a message


# Function to open WhatsApp and send a message
def openWhatsAppAndSendMessage():
    speak("Whom do you want to send a message to on WhatsApp? Please include the country code.")
    contact_name = takeCommand()

    # Open WhatsApp Web in the default web browser
    webbrowser.open("https://web.whatsapp.com/")

    # Wait for the user to scan the QR code
    speak("Please scan the QR code on your screen.")

    # Wait for the user to confirm after scanning
    while True:
        response = takeCommand().lower()
        if 'yes' in response:
            break
        else:
            speak("Please say 'yes' when you have scanned the QR code.")

    # Ask for the message to be sent
    speak("What message do you want to send?")
    message = takeCommand()

    # Use pyperclip to copy the message to the clipboard
    pyperclip.copy(message)

    # Type the contact name
    time.sleep(2)  # Add a delay for WhatsApp to fully load
    pyautogui.click(x=200, y=200)  # Click on the chat box

    # Type the contact name (you may need to adjust the coordinates based on your screen)
    pyautogui.write(contact_name)
    time.sleep(1)
    pyautogui.press('enter')

    # Simulate Ctrl + V (paste) to input the message
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')

    speak("Message sent.")


# Function for a simple calculator
def simpleCalculator():
    speak("Please provide a mathematical expression.")
    expression = takeCommand()

    try:
        result = eval(expression)
        speak(f"The result is {result}.")
    except Exception as e:
        speak("Sorry, I couldn't evaluate the expression.")
# Function to set an alarm
def setAlarm():
    speak("What time would you like to set the alarm for? Please provide the time in 24-hour format.")
    alarm_time = takeCommand().lower()

    try:
        alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M")
        current_time = datetime.datetime.now().time()
        
        while datetime.datetime.now().time() < alarm_time.time():
            time.sleep(1)

        speak("Time to wake up!")
    except Exception as e:
        speak("Invalid time format. Please provide the time in 24-hour format.")
# Function to tell a joke
def tellJoke():
    # You can use a joke API or provide predefined jokes
    speak("Why did the programmer go broke? Because he used up all his cache.")
# Function to adjust device volume
# Function to adjust device volume
def adjustVolume():
    speak("Do you want to increase or decrease the volume?")
    command = takeCommand().lower()

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    if 'increase' in command or 'up' in command:
        current_volume = volume.GetMasterVolumeLevelScalar()
        new_volume = min(1.0, current_volume + 0.1)  # Increase by 0.1 (10%)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        speak("Volume increased.")
    elif 'decrease' in command or 'down' in command:
        current_volume = volume.GetMasterVolumeLevelScalar()
        new_volume = max(0.0, current_volume - 0.1)  # Decrease by 0.1 (10%)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        speak("Volume decreased.")
    else:
        speak("Invalid command. Please specify 'increase' or 'decrease'.")

class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        master.title("Voice Assistant")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Voice Assistant", command=self.start_assistant)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Voice Assistant", command=self.stop_assistant, state=tk.DISABLED)
        self.stop_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=master.destroy)
        self.exit_button.pack()

        self.running = False
        self.assistant_thread = None

    def start_assistant(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.assistant_thread = Thread(target=self.run_assistant)
            self.assistant_thread.start()

    def stop_assistant(self):
        if self.running:
            self.running = False
            self.stop_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)
            self.assistant_thread.join()

    def run_assistant(self):
        while self.running:
            query = takeCommand()
            # Process user query and execute assistant functions
            if 'exit' in query:
                speak("Goodbye! Have a great day.")
                self.stop_assistant()
            else:
                response = chatGPT(query)
                speak(response)
                self.text_area.insert(tk.END, f"User: {query}\nAssistant: {response}\n\n")
                self.text_area.see(tk.END)  # Auto-scroll to the bottom


# Main execution loop
if __name__ == "__main__":
    root = tk.Tk()
    gui = VoiceAssistantGUI(root)
    root.mainloop()
    chatWithGPT()
    speak("Hello! How can I assist you today?")

    while True:
        query = takeCommand()

        
        if 'open youtube' in query:
            openYouTube()
        elif 'search on youtube' in query:
            speak("What do you want to search on YouTube?")
            search_query = takeCommand()
            searchYouTube(search_query)
        elif 'open google' in query:
            speak("What do you want to search on Google?")
            search_query = takeCommand()
            searchGoogle(search_query)
        elif 'create different shapes' in query:
            createShapes()
        elif 'open gmail' in query:
            createEmail()
        elif 'open notepad and write' in query:
            speak("What message would you like to write in Notepad?")
            notepad_message = takeCommand()
            writeNotepadMessage(notepad_message)
        elif 'open wordpad and type' in query:
            speak("What message would you like to type in WordPad?")
            wordpad_message = takeCommand()
            typeWordpadMessage(wordpad_message)
        elif 'tell temperature' in query:
            tellTemperature()
        elif 'tell date' in query:
            tellDate()
        elif 'tell time' in query:
            tellTime()
        elif 'open chrome' in query:
            openChrome()
        elif 'open settings' in query:
            openSettings()
        elif 'create folder' in query:
            speak("What should be the name of the folder?")
            folder_name = takeCommand()
            createFolder(folder_name)
        elif 'open camera and take picture' in query:
            openCameraAndTakePicture()
        elif 'take screenshot' in query:
            takeScreenshot()
        elif 'translate to hindi' in query:
            translateToHindi()
        elif 'play rock paper scissors' in query:
            playRockPaperScissors()
        elif 'check internet speed' in query:
            checkInternetSpeed()
        elif 'shut down system' in query:
            shutDownSystem()
        elif 'open whatsapp and send message' in query:
            openWhatsAppAndSendMessage()
        elif 'simple calculator' in query:
            simpleCalculator()
        elif 'volume up' in query:
            adjustVolume('up')
        elif 'volume down' in query:
            adjustVolume('down')
        elif 'set alarm' in query:
            setAlarm()
        elif 'tell me a joke' in query:
            tellJoke()
        elif 'adjust the volume' in query:
            adjustVolume()
        elif 'exit' in query:
            speak("Goodbye! Have a great day.")
            break
