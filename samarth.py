import tkinter as tk
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import sched
import subprocess
import pyaudio
import pywhatkit
import requests
import os.path
import pyautogui
# from Google import create_service
# import base64
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import geocoder
# from gtts import gTTS


# pywhatkit.start_server()
# from apikey import api_data


# def on_button_click(question):
#     query = takeCommand().lower()
#     text_widget.insert(tk.END, f"User: {query}\n")
#     prompt = f'Samarth:{question}\n'
#     response = completion.create(prompt=prompt, engine="text-davini-002")
#     answer = response.choices[0].text.strip()
#     text_widget.insert(tk.END, f"Samarth: {answer}\n", speak(answer))
#     return answer


# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# Function to speak a given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



# Updated function to speak and insert into text widget
def speak_and_insert(audio):
    engine.say(audio)
    engine.runAndWait()
    text_widget.insert(tk.END, f"Samarth: {audio}\n")


# Function to greet the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("hi Good Evening!")
    speak("Hello well, I am Saamarth (an artificially intelligent personal assistant), please tell me how may I help you")

# def sendEmail(to, content):
#     # New feature: Sending email using Gmail API
#     CLIENT_SECRET_FILE = 'acct1.json'
#     API_NAME = 'gmail'
#     API_VERSION = 'v1'
#     SCOPES = ['https://mail.google.com/']

#     service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#     emailMsg = content
#     mimeMessage = MIMEMultipart()
#     mimeMessage['to'] = to
#     mimeMessage['subject'] = 'Subject of the email'
#     mimeMessage.attach(MIMEText(emailMsg, 'plain'))
#     raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

#     message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
#     print(message)    
#     speak("Email has been sent")    

def takeEmailCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for email....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing email.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        email_command = query.lower().replace(" ", "")  # Convert to lowercase and remove spaces
        return email_command
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"



# def get_location():
#     # Get current location using IP address
#     location = geocoder.ip('me')

#     # Access different attributes of the location
#     city = location.city
#     state = location.state
#     country = location.country
#     # latitude = location.latlng[0]
#     # longitude = location.latlng[1]

#     return city, state, country#, latitude, longitude

def speakLocation(city, state, country): #, latitude, longitude):
    speak(f"Your current location is in {city}, {state}, {country}")#. The latitude is {latitude} and the longitude is {longitude}.")


# Function to handle the button click event
def on_button_click():
    query = takeCommand().lower()
    text_widget.insert(tk.END, f"User: {query}\n")

    if 'wikipedia' in query:
        speak('ok Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("so, According to Wikipedia")
        text_widget.insert(tk.END, "Samarth: According to Wikipedia\n")
        text_widget.insert(tk.END, f"Samarth: {results}\n", speak(results))

    elif 'open chrome' in query:
        speak("Opening Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'search in chrome' in query:
        speak("What do you want to search in Chrome?")
        search_query = takeCommand()
        speak(f"Searching in Chrome for {search_query}")
        pywhatkit.search(search_query)

    elif 'scroll down' in query:
        speak("Scrolling down")
        pyautogui.scroll(3)

    elif 'scroll up' in query:
        speak("Scrolling up")
        pyautogui.scroll(-3)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'C:\\Path\\To\\Your\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))


    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'message' in query:
        try:
            speak("Please provide the phone number")
            P_No = takeCommand()
            speak("What message do you want to send?")
            msg = takeCommand()
            sendWhatsappMessage(P_No, msg)
            speak("WhatsApp message has been sent")
        except Exception as e:
            print(e)
            speak("Sorry, I am not able to send this WhatsApp message")

    elif 'open code' in query:
        codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    # elif 'email' in query:
    #     try:
    #         speak("What should I say?")
    #         content = takeCommand()
    #         speak("Please provide the recipient's email address.")
    #         to = takeEmailCommand()  # Use takeEmailCommand to handle email more accurately
    #         sendEmail(to, content)
            

           
        # except Exception as e:
        #     print(e)
        #     speak("Sorry, I am not able to send this email!")

    elif 'add note' in query:
        speak("What would you like to add to your notes?")
        note_text = takeCommand()
        addNote(note_text)

    elif 'get notes' in query:
        getNotes()

    elif 'weather' in query:
        speak("Please provide the city name")
        city_name = takeCommand()
        getWeather(city_name)
    
    # elif 'location' in query:
    #     city, state, country, latitude, longitude = get_location()
    #     speakLocation(city, state, country, latitude, longitude)


# Function to send a WhatsApp message
def sendWhatsappMessage(phone_number, message):
    pywhatkit.sendwhatmsg_instantly(phone_number, message)


# Function to add a note to a file
def addNote(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    speak("Note added successfully")


# Function to get and speak notes from a file
def getNotes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        for note in notes:
            speak(note.strip())
    except FileNotFoundError:
        speak("No notes found")


# Function to get and speak weather information for a city
def getWeather(city):
    api_key = "your_weather_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        weather_info = data["weather"][0]["description"]
        speak(f"The weather in {city} is {weather_info}")
    else:
        speak("City not found")




# Function to listen to user's command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"


# Initialize the GUI
root = tk.Tk()
root.title("Samarth AI")
root.geometry("400x400")

# Create a text widget to display the conversation
text_widget = tk.Text(root, height=15, width=40)
text_widget.pack(padx=10, pady=10)

# Create a button to start listening
button = tk.Button(root, text="Listen", command=on_button_click)
button.pack(pady=10)

# Start by greeting the user
wishMe()

# Run the GUI main loop
root.mainloop()






# import speech_recognition as sr
# import pyttsx3
# import mysql.connector

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def recognize_speech():
#     recognizer = sr.Recognizer()
    
#     with sr.Microphone() as source:
#         speak("Please say the contact name:")
#         print("Please say the contact name:")
#         recognizer.adjust_for_ambient_noise(source)
#         name_audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
#         speak("Name recorded, now please say the phone number:")
#         print("Name recorded, now please say the phone number:")
#         recognizer.adjust_for_ambient_noise(source)
#         phone_audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

#     try:
#         name = recognizer.recognize_google(name_audio).lower()
#         phone = recognizer.recognize_google(phone_audio)
#         speak(f"Name recognized as {name}. Phone number recognized as {phone}.")
#         print(f"Name: {name}, Phone: {phone}")
#         return name, phone
#     except sr.UnknownValueError:
#         speak("Sorry, could not understand the input.")
#         print("Sorry, could not understand the input.")
#         return None, None
#     except sr.RequestError as e:
#         speak(f"Error making the request: {e}")
#         print(f"Error making the request: {e}")
#         return None, None

# def store_in_database(name, phone):
#     connection = None
#     try:
#         connection=mysql.connector.connect(host="localhost",user="root",password="",database="jarvis")
#         cursor = connection.cursor()
#         query = "INSERT INTO contact (name, phone) VALUES (%s, %s)"
#         values = (name, phone)
#         cursor.execute(query, values)

#         connection.commit()
#         speak("Contact successfully stored in the database!")
#         print("Contact successfully stored in the database!")

#     except mysql.connector.Error as err:
#         speak(f"Error: {err}")
#         print(f"Error: {err}")
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()

# if __name__ == "__main__":
#     speak("Welcome to the contact storage system. Please provide contact details.")
#     name, phone = recognize_speech()

#     if name and phone:
#         store_in_database(name, phone)
































# import tkinter as tk
# from tkinter import messagebox
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# import time
# import sched
# import subprocess
# import openai
# import pywhatkit
# pywhatkit.start_server()
# from apikey import api_data
# openai.api_key = api_data
# completion = openai.Completion()




# def on_button_click(question):
#     query = takeCommand().lower()
#     text_widget.insert(tk.END, f"User: {query}\n")
#     prompt=f'Samarth:{question}\n'
#     response = completion.create(prompt=prompt, engine= "text-davini-002")
#     answer = response.choices[0].text.strip()
#     text_widget.insert(tk.END, f"Samarth: {answer}\n", speak(answer))
#     return answer




# # Initialize the speech engine
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)

# # Function to speak a given audio
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# # Updated function to speak and insert into text widget
# def speak_and_insert(audio):
#     engine.say(audio)
#     engine.runAndWait()
#     text_widget.insert(tk.END, f"Samarth: {audio}\n")



# # Function to greet the user
# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if 0 <= hour < 12:
#         speak("GGGood Morning!")
#     elif 12 <= hour < 18:
#         speak("GGGood Afternoon!")
#     else:
#         speak("hi Good Evening!")
#     speak("Hello well, I am Saamarth (an artificially intelligent personal assistant), please tell me how may I help you")

# # Function to handle the button click event

# def on_button_click():
#     query = takeCommand().lower()
#     text_widget.insert(tk.END, f"User: {query}\n")

#     if 'wikipedia' in query:
#         speak('ok Searching Wikipedia....')
#         query = query.replace("wikipedia", "")
#         results = wikipedia.summary(query, sentences=2)
#         speak("so, According to Wikipedia")
#         text_widget.insert(tk.END, "Samarth: According to Wikipedia\n")
#         text_widget.insert(tk.END, f"Samarth: {results}\n", speak(results))
        
#     elif 'open youtube' in query:
#         webbrowser.open("https://www.youtube.com")
#     elif 'open google' in query:
#         webbrowser.open("https://www.google.com")
#     elif 'open stackoverflow' in query:
#         webbrowser.open("https://www.stackoverflow.com")
#     # elif 'set reminder' in query:
#     #     def set_reminder(reminder_voice, delay_in_seconds):
#     #         schedule = sched.schedule(time.time, time.sleep)
#     #         schedule.enter(delay_in_seconds, 1, lambda: print(f"Reminder: {reminder_text}"))
#     #         schedule.run()

#         # speak("What should I remind you about?")
#         # reminder_voice = takeCommand().lower()
#         # speak("In how many seconds should I remind you?")
#         # delay_seconds = int(takeCommand().lower())
#         # set_reminder(reminder_voice, delay_seconds)
#         # speak(f"I will remind you about {reminder_voice} in {delay_seconds} seconds. ")

#     elif "open calendar" in query:
#         # Function to open the Microsoft Calendar on windows
#         def open_microsoft_calendar():
#             try:
#                 subprocess.run(["start", "outlookcal:"])
#                 speak("Opening Microsoft Calendar.")
#             except Exception as e:
#                 print(f"Error: {e}")
#                 speak("Sorry, I couldn't open Microsoft Calendar.")
        
#         open_microsoft_calendar()

#     elif "whatsapp" in query:
#         speak("Give me the number to whom you want to send message including +91")
#         contact_number = takeCommand().lower()
#         speak("What is you message")
#         message = takeCommand().lower()
#         speak("At what time in hour according to 24 hour clock do want to send the message")
#         hour = int(takeCommand().lower())
#         speak("At what time in minute do want to send the message")
#         minute = int(takeCommand().lower())
#         pywhatkit.sendwhatmsg(contact_number, message, hour, minute)
#         speak(f"I will send your message which says {message} to {contact_number} at {hour, minute}")
        
           


#     elif 'play music' in query:
#         music_dir = 'D:\\Music'  # Replace with your music directory
#         songs = os.listdir(music_dir)
#         os.startfile(os.path.join(music_dir, songs[0]))
#     elif 'the time' in query:
#         strTime = datetime.datetime.now().strftime("%H:%M:%S")
#         speak(f"Sir, the time is {strTime}")
#         text_widget.insert(tk.END, f"Samarth: Sir, the time is {strTime}\n")
#     # elif 'the time' in query:
#     #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
#     #     speak_and_insert(f"Sir, the time is {strTime}")
        

#     elif 'open code' in query:
#         codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#         os.startfile(codePath)
#     else:
#         speak("Sorry, I didn't understand that.")

# # Function to listen to user's command
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening....")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing.....")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You said: {query}\n")
#         return query
#     except Exception as e:
#         print(e)
#         print("Say that again please....")
#         return "None"

# # Initialize the GUI
# root = tk.Tk()
# root.title("Samarth AI")
# root.geometry("400x400")

# # Create a text widget to display the conversation
# text_widget = tk.Text(root, height=15, width=40)
# text_widget.pack(padx=10, pady=10)

# # Create a button to start listening
# button = tk.Button(root, text="Listen", command=on_button_click)
# button.pack(pady=10)

# # Start by greeting the user
# wishMe()

# # Run the GUI main loop
# root.mainloop()




























# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# import smtplib
# import pywhatkit
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# import requests
# import os.path
# import pyautogui



# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# # print(voices)
# # print(voices[0.id)
# engine.setProperty("voice", voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")
    
#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")
#     # 
#     else:
#         speak("Good Evening!")

#     speak("I am Jarvis sir, Please tell me how may I help you")

# def takeCommand():# (alag se docstrings sikhna)
#     #it takes microphone input from the use and returns string output
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening....")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing.....")
#         query = r.recognize_google(audio, language='en.in')
#         print(f"User said: {query}\n") #fstring

#     except Exception as e:
#         # print(e)
#         print("Say that again please....")
#         return "None"
#     return query

# # def sendEmail
# def sendEmail(to, content):
#     # Configure your email credentials
#     sender_email = "your_email@gmail.com"
#     sender_password = "your_app_specific_password"

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, to, content)
#         server.close()
#     except Exception as e:
#         print(e)

# #def whatsapp
# def sendWhatsappMessage(phone_number, message):
#     pywhatkit.sendwhatmsg_instantly(phone_number, message)


# def addNote(note):
#     with open("notes.txt", "a") as file:
#         file.write(note + "\n")
#     speak("Note added successfully")


# def getNotes():
#     try:
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()
#         for note in notes:
#             speak(note.strip())
#     except FileNotFoundError:
#         speak("No notes found")


# def getWeather(city):
#     api_key = "your_weather_api_key"
#     base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#     response = requests.get(base_url)
#     data = response.json()
#     if data["cod"] != "404":
#         weather_info = data["weather"][0]["description"]
#         speak(f"The weather in {city} is {weather_info}")
#     else:
#         speak("City not found")


# # def translate(text, target_language="en"):
# #     translator = Translator()
# #     translated_text = translator.translate(text, lang_tgt=target_language)
# #     speak(f"The translation is: {translated_text}")

# query = takeCommand().lower()
# if __name__ == "__main__":
#     # speak("Ronak is a good boy")
#     wishMe()
#     while True:
#         query = takeCommand().lower()

#         # Logic for executing task based on query
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia....')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=5)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)

#         elif 'open chrome' in query:
#             speak("Opening Chrome")
#             webbrowser.open("chrome.exe")

#         elif 'search in chrome' in query:
#             speak("What do you want to search in Chrome?")
#             search_query = takeCommand()
#             speak(f"Searching in Chrome for {search_query}")
            
#             # Simulate typing in Chrome address bar and pressing Enter
#             pyautogui.hotkey('ctrl', 'l')  # Selects the address bar
#             pyautogui.write(search_query, interval=0.1)  # Types the search query
#             pyautogui.press('enter')  # Presses Enter

#         elif 'scroll down' in query:
#             speak("Scrolling down")
#             pyautogui.scroll(3)

#         elif 'scroll up' in query:
#             speak("Scrolling up")
#             pyautogui.scroll(-3)

#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")

#         elif 'open google' in query:
#             webbrowser.open("google.com")

#         elif 'open stackoverflow' in query:
#             webbrowser.open("stackoverflow.com")

#         elif 'play music' in query:
#             music_dir = 'D:\\Music'
#             songs = os.listdir(music_dir)
#             print(songs)
#             os.startfile(os.path.join(music_dir,songs[0]))

            
#         elif 'time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"Sir, the time is {strTime}")

#         elif 'message' in query:
#             try:
#                 speak("Please provide the phone number")
#                 P_No = takeCommand()
#                 speak("what message do you want to send?")
#                 msg = takeCommand()
#                 sendWhatsappMessage(P_No, msg)
#                 speak("whatsapp message has ben sent")
#             except Exception as e:
#                 print(e)
#                 speak("Soory, I am not able to send this whatsapp message")
 
#         elif 'open code' in query:
#             codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#             os.startfile(codePath)

#         elif 'email' in query:
#             try:
#                 speak("What should I say?")
#                 content= takeCommand()
#                 to = "ronakgupta3305@gmail.com"
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry. I am not able to send this email!")
        
#         elif 'add note' in query:
#             speak("What would you like to add to your notes?")
#             note_text = takeCommand()
#             addNote(note_text)

#         elif 'get notes' in query:
#             getNotes()

#         elif 'weather' in query:
#             speak("Please provide the city name")
#             city_name = takeCommand()
#             getWeather(city_name)
        


        # elif 'translate' in query:
        #     speak("What text would you like to translate?")
        #     text_to_translate = takeCommand()
        #     speak("In which language would you like to translate?")    
        #     target_language = takeCommand().lower()
        #     translate(text_to_translate, target_language)
            
        





























# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# import smtplib
# import pywhatkit
# import requests
# import json

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak("Good Morning!")
#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon!")
#     else:
#         speak("Good Evening!")

#     speak("I am Jarvis, sir. Please tell me how may I help you")

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening....")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing.....")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")
#     except Exception as e:
#         print("Say that again please....")
#         return "None"
#     return query

# def sendEmail(to, content):
#     # Configure your email credentials
#     sender_email = "your_email@gmail.com"
#     sender_password = "your_app_specific_password"

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, to, content)
#         server.close()
#     except Exception as e:
#         print(e)

# def sendWhatsappMessage(phone_number, message):
#     pywhatkit.sendwhatmsg_instantly(phone_number, message)

# def get_note():
#     speak("Here are your notes")
#     with open("notes.txt", "r") as f:
#         notes = f.readlines()
#         for note in notes:
#             speak(note)

# def add_note():
#     try:
#         speak("Please tell me what you want me to note down")
#         note = takeCommand()
#         with open("notes.txt", "a") as f:
#             f.write(note)
#             f.write("\n")
#         speak("I have added the note to the notes.txt file")
#     except Exception as e:
#         print(e)
#         speak("Sorry, I am unable to create a note.")

# def get_weather():
#     try:
#         api_key = "Your_API_Key"
#         base_url = "http://api.openweathermap.org/data/2.5/weather?"
#         speak("what is the city name?") 
#         city_name = takeCommand() 
#         complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#         response = requests.get(complete_url)
#         data = response.json()
#         if data['cod'] != '404':
#             main = data['main']
#             weather_report = main['temp']
#             print(weather_report)
#             speak(f"The weather report for {city_name} is: {weather_report}")
#         else:
#             speak("City not found! Please check the spelling.")
#     except Exception as e:
#         print(e)
#         speak("Unable to get the weather report.")

# def get_translation():
#     try:
#         api_key = "Your_Translator_API_Key"
#         base_url = "https://translation.googleapis.com/language/translate/v2?key="
#         source = "en"
#         target = "es"
#         speak("what is the text?")
#         text = takeCommand()
#         complete_url = base_url + api_key + "&q=" + text + "&source=" + source + "&target=" + target
#         response = requests.get(complete_url)
#         data = response.json()
#         translation = data['data']['translations'][0]['translatedText']
#         print(translation)
#         speak(f"The translation of the text is: {translation}")
#     except Exception as e:
#         print(e)
#         speak("Unable to get the translation.")

# def get_translation_language():
#     try:
#         api_key = "Your_Translator_API_Key"
#         base_url = "https://translation.googleapis.com/language/translate/v2?key="
#         source = take_command()
#         target = "es" speak("what is the text?")
#         target = take_command()
#         speak("what is the text?")
#         text = take_command()
#         complete_url = base_url + api_key + "&q=" + text + "&source=" + source + "&target=" + target
#         response = requests.get(complete_url)
#         data = response.json()
#         translation = data['data']['translations'][0]['translatedText']
#         print(translation)
#         speak(f"The translation of the text is: {translation}")
#     except Exception as e:
#         print(e)
#         speak("Unable to get the translation.")

# if __name__ == "__main__":
#     wishMe()
#     while True:
#         query = takeCommand().lower()

#         if 'wikipedia' in query:
#             speak('Searching Wikipedia....')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=5)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)

#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")

#         elif 'open google' in query:
#             webbrowser.open("google.com")

#         elif 'open stackoverflow' in query:
#             webbrowser.open("stackoverflow.com")

#         elif 'play music' in query:
#             music_dir = 'D:\\Music'
#             songs = os.listdir(music_dir)
#             print(songs)
#             os.startfile(os.path.join(music_dir,songs[0]))

#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"Sir, the time is {strTime}")

#         elif 'open code' in query:
#             codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#             os.startfile(codePath)

#         elif 'email' in query:
#             try:
#                 speak("What should I say?")
               
