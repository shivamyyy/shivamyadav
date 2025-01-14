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
import screen_brightness_control as sbc
import pyautogui
import pyjokes
import shutil
import json
import smtplib
import wolframalpha
from urllib.request import urlopen
import time
import wmi
DEFAULT_COUNTRY_CODE = "+91"
import pyperclip
# # import openai
# openai.api_key = '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'

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
    
# # Function to interact with ChatGPT API
# def chatGPT(message):
#     response = openai.Completion.create(
#     engine="gpt-3.5-turbo-instruct",  # Use a supported model like text-davinci-003
#     prompt=message,
#     max_tokens=150
# )

#     return response.choices[0].text.strip()

# # Function to chat with ChatGPT
# def chatWithGPT():
#     speak("How can I assist you today?")
#     while True:
#         user_input = takeCommand()
#         if 'switch' in user_input:
#             speak("switching to normal mode")
#             break

#         # Send user input to ChatGPT
#         response = chatGPT(user_input)

#         # Speak the response from ChatGPT
#         speak(response)
#         # Display the response in text format
#         print("Assistant:", response)

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

# Function to open WhatsApp and send a message
# Function to open WhatsApp and send a message
def openWhatsAppAndSendMessage():
    speak("Whom do you want to send a message to?")
    recipient_number = takeCommand()
    recipient_number = takeCommand()

    # If country code is not included, prepend the default
    if not recipient_number.startswith("+"):
        recipient_number = DEFAULT_COUNTRY_CODE + recipient_number

    print("Recipient Number:", recipient_number) 

    speak("What message do you want to send?")
    message = takeCommand()

    # Use pywhatkit to send the message
    kit.sendwhatmsg_instantly(recipient_number, message, wait_time=10)  # Adjust wait_time if needed
    speak("Message sent to " + recipient_number + " on WhatsApp.")





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

# Function to adjust device volume

# Function to adjust device volume
def adjustVolume(command):
    # Get the default audio playback device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Use _iid_ instead of iid
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

# Function to toggle Wi-Fi


# Function to open File Explorer
def openFileExplorer():
    os.startfile('explorer.exe')

def increaseBrightness():
    current_brightness = sbc.get_brightness()[0]  # Extract the brightness value
    new_brightness = min(100, current_brightness + 10)  # Increase by 10%
    sbc.set_brightness(new_brightness)
    speak("Brightness increased.")

def decreaseBrightness():
    current_brightness = sbc.get_brightness()[0]  # Extract the brightness value
    new_brightness = max(0, current_brightness - 10)  # Decrease by 10%
    sbc.set_brightness(new_brightness)
    speak("Brightness decreased.")


# Function to shut down the system
def shutDownSystem():
    speak("Are you sure you want to shut down the system?")
    confirmation = takeCommand().lower()

    if 'yes' in confirmation:
        os.system("shutdown /s /t 1")
    else:
        speak("Shutting down cancelled.")

# Function to restart the system
def restartSystem():
    speak("Are you sure you want to restart the system?")
    confirmation = takeCommand().lower()

    if 'yes' in confirmation:
        os.system("shutdown /r /t 1")
    else:
        speak("Restarting cancelled.")

# Function to search on the web
def searchWeb(query):
    query = query.replace("search", "").replace("play", "").strip()
    if query:
        webbrowser.open(query)
    else:
        speak("Please provide a valid search query.")

def sendEmail():
    try:
        speak("To whom do you want to send the email?")
        to = input("Recipient's Email: ").strip()

        speak("What should be the subject of the email?")
        subject = input("Subject: ")

        speak("What message would you like to send?")
        content = input("Message: ")

        # Open Gmail in the default web browser
        webbrowser.open("https://mail.google.com")

        # Wait for Gmail to open
        time.sleep(5)

        # Compose the email by simulating key presses
        pyautogui.hotkey('c')  # 'c' for compose
        time.sleep(2)

        pyautogui.write(to)
        pyautogui.press('tab')  # Move to the subject field
        time.sleep(1)
        pyautogui.write(subject)
        pyautogui.press('tab')  # Move to the message body
        time.sleep(1)
        pyautogui.write(content)

        # Send the email
        pyautogui.hotkey('ctrl', 'enter')

        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")








# Main execution loop
if __name__ == "__main__":
    # chatWithGPT()
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
    
        elif 'play rock paper scissors' in query:
            playRockPaperScissors()
        elif 'check internet speed' in query:
            checkInternetSpeed()
        elif 'open whatsapp and send message' in query:
            openWhatsAppAndSendMessage()

        elif 'news' in query:
             
            try: 
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "").replace("play", "").strip()
            searchWeb(query)

        elif 'send a email' in query:
            sendEmail()

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        
        elif "where is" in query:
                    location = query.replace("where is", "").strip()
                    speak(f"Locating {location}")
                    webbrowser.open(f"https://www.google.com/maps/place/{location}")



        elif 'shut down' in query:
            shutDownSystem()

        elif 'restart' in query:
            restartSystem()
        elif 'open file explorer' in query:
            openFileExplorer()
        elif 'increase brightness' in query:
            increaseBrightness()
        elif 'decrease brightness' in query:
            decreaseBrightness()
        elif 'set brightness to' in query:
            try:
                new_brightness = int(query.split("to")[-1])  # Extract brightness value
                sbc.set_brightness(new_brightness)
                speak(f"Brightness set to {new_brightness}%.")
            except ValueError:
                speak("Invalid brightness value. Please specify a number between 0 and 100.")
        elif 'volume up' in query or 'increase volume' in query:
            adjustVolume(query)
        elif 'volume down' in query or 'decrease volume' in query:
            adjustVolume(query)
        elif 'set alarm' in query:
            setAlarm()

        elif 'adjust the volume' in query:
            adjustVolume()
        elif 'exit' in query:
            speak("Goodbye! Have a great day.")
            break
