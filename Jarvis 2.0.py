'''This personal assistant can do the following tasks:-
    1. Can greet the user as per the time
    2. Can tell random jokes to the user 
    3. Can open youtube and google 
    4. Can search any topic on google 
    5. Can play any video on youtube
    6. Can search a topic on wikipedia and speak the meaning of it 
    7. Can open a file in your PC
    8. Can tell the time to it's user
    9. Can add, subtract, divid, and multiply two numbers
    10.Can take to the user
    11.Can check the battery percentage in your device 
    12.Can control volume of the computer
    13.Can tell the weather outside
    14.Can add a task which you need to complete.
    15.Can remove a task.
    16.Can add task to completed list.
    17.Can show completed tasks.
    18.Can show task to complete
'''

# These are all the modules which we will need for making our Personal Assistant

import pyttsx3 # import this from pip 
import time
import speech_recognition as sr # import this from pip
import wikipedia    # import this from pip 
import datetime
import webbrowser
import random  # import this from pip
import pywhatkit  # import this from pip
import pyjokes # import this from pip
import os
import psutil # import this from pip
import pyautogui # import this from pip
import requests
from bs4 import BeautifulSoup   # import from pip


# These line of code will use sapi5 voice API to let the AI to speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

# This function will speak all the lines that we want

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# This class contains the function of greeting the user as per the time and take command from the microphone
class Jarvis():

    
    # This function will greet user
    @staticmethod    
    def greeting():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak('Good Morning')
        elif hour>=12 and hour<17:
            speak('Good Afternoon')
        else:
            speak('Good Evening')
        speak('Boss, how may i help you')

    # This function will take command from the user through microphone in english
    @staticmethod
    def Takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            r.dynamic_energy_adjustment_damping = 0.15
            audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') 
            print(f"User said: {query}\n") 

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

# This User_command class will contain all the commands that can  be followed by our Personal Assistant 

class User_commands:

    #This function will speak hello to the user if the user says 'hello'
    @staticmethod
    def say_hello():
        speak('Hello!!, boss')
    
    #This function will let the AI speak his name
    @staticmethod
    def tell_name(): 
        speak('My name is jarvis')
    
    # This function will tell the time with the help of time module 
    @staticmethod
    def tell_time():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"boss, the time is {strTime}")

    # This function will open youtube.com with the help webbrowser module 
    @staticmethod
    def open_youtube():
        webbrowser.open("youtube.com")

    # This funtion will also open google.com with the help of webbrowser module
    @staticmethod
    def open_google():
        webbrowser.open('google.com')

    # This function will speak a random joke with the help of pyjokes module
    @staticmethod
    def tell_jokes():
        speak(pyjokes.get_joke(language='en', category='all'))

    # This function will search the query of the user on google with the help of pywhatkit module
    @staticmethod
    def search_google():
        speak('Boss, what should i search on Google')
        search = Jarvis.Takecommand()
        pywhatkit.search(search)
        speak(f'Searching {search} on google')
    
    # This function will start play the youtube video which the user will say with the help of pywhatkit module
    @staticmethod
    def play_youtube_video():
        speak('Boss, which video you want me to play on youtube')
        video = Jarvis.Takecommand()
        pywhatkit.playonyt(video)
        speak(f'Starting {video} on Youtube')
    
    @staticmethod
    def check_battery():
        battery = psutil.sensors_battery()    
        percentage = battery.percent
        speak(f'Boss the battery persentage is {percentage}.')
        if percentage <25:
            speak('Boss I think you need to charge your device.')
        else:
            speak('Battery percentage will be enough for your work.')

    # This function will tell the weather

    @staticmethod
    def tell_weather():
        search = 'weather outside'
        url = f'https://www.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text, 'html.parser')
        weather = data.find("div", class_="BNeawe").text
        speak(f'Boss, the {search} is {weather}')

    # These function will control the volume of the computer
    @staticmethod
    def volume_up():
        pyautogui.press('volumeup')
    
    @staticmethod
    def volume_down():
        pyautogui.press('volumedown')
    
    @staticmethod
    def mute():
        pyautogui.press('volumemute')

    
    # This function will open the path of the file given with the help of os module
    @staticmethod
    def open_vscode():
        path = 'C:\\Users\\saiya\\AppData\\Local\\Programs\\Microsoft VS Code'
        os.startfile(path)
    
    # This function will calcuate the numbers.
    @staticmethod
    def calculate():
        speak('Boss ,what is the first number??')
        num1 = int(Jarvis.Takecommand())
        speak('What is the opparation??')
        op = Jarvis.Takecommand()
        speak('What is the second number??')
        num2 = int(Jarvis.Takecommand())
        if op=='plus':
            speak(f'The sum of {num1} and {num2} is {num1+num2}')
            print(num1+num2)
        elif op=='minus':
            speak(f'The difference of {num1} and {num2} is {num1-num2}')
            print(num1-num2)
        elif op=='divid':
            speak(f'The answer is {num1/num2}')
            print(num1/num2)
        elif op=='multiply':
            speak(f'The product of {num1} and {num2} is {num1} is {num1*num2}')
            print(num1*num2)
        else:
                speak('Boss, there is a problem solving this.')

    # This function will add a task which the user woll say to a different file.
    @staticmethod
    def add_task():
        speak('Boss, please tell the task which you want to add')
        task = Jarvis.Takecommand()
        with open('all_task.txt', 'a') as f:
            f.write(f'\n{task}')
        speak('Boss, i have added this task in your To-Do-List.')


    @staticmethod
    def tell_pending_tast():
            with open('all_task.txt', 'r') as f:
                tasks = str(f.read())
                speak('Boss, here are all the tasks you need to do.')
                print(tasks)

    @staticmethod
    def remove_a_task():
        speak('Boss, which task do you want me to remove??')
        entry = Jarvis.Takecommand()
        fn = 'all_task.txt'
        f = open(fn)
        output = []
        task_deleted = entry
        for line in f:
            if not line.startswith(task_deleted):
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()
        speak('Boss, i have removed this task.')
    
    @staticmethod
    def add_task_to_complete():
        speak('Boss, please tell the task which you have completed.')
        user_entry = Jarvis.Takecommand()
        entry = Jarvis.Takecommand()
        fn = 'all_task.txt'
        f = open(fn)
        output = []
        task_deleted = entry
        for line in f:
            if not line.startswith(task_deleted):
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()

        with open('campleted_tasts.txt', 'a') as f:
            f.write(f'\n{user_entry}')
        speak('Boss, i have added this task to completed list.')

    @staticmethod
    def show_completed_task():
        with open('completed_tasks.txt', 'r') as f:
           task = f.read()
           speak('Boss, here are the completed tasks.')
           print(f'Completed task - {task}')


if __name__ == "__main__":
    Jarvis.greeting()
    Jarvis.Takecommand()
    while True:
        query = Jarvis.Takecommand().lower()

        if 'hello' in query:
            User_commands.say_hello()
        
        elif 'ok jarvis' in query:
            speak('Yes boss')
        
        elif 'how are you' in query:
            speak('I am fine boss thanks for asking, How are you?')

            answer = Jarvis.Takecommand()
            if 'fine' in answer:
                speak('Ohh, that is great!!')
            elif 'good' in answer:
                speak('Ohh, that is great!!')
            else:
                speak('Is there any thing that i can help you with???')
        
        elif 'what is your name' in query:
            User_commands.tell_name()
        
        elif  'who is the best' in query:
            speak('Saiyam Arora is the best in this world.')

        elif 'work' in query or 'tasks' in query:
            User_commands.tell_pending_tast()
        
        elif 'add a task' in query or 'add work' in query:
            User_commands.add_task()
        
        elif 'add a task to complete' in query or 'add work to complete' in query:
            User_commands.add_task_to_complete()
        
        elif 'remove a task' in query or 'delete a task' in query:
            User_commands.remove_a_task()
        
        elif 'show all my completed tasks' in query or 'show completed task' in query:
            User_commands.show_completed_task()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'battery' in query:
            User_commands.check_battery()
        
        elif 'volume up' in query:
            User_commands.volume_up()
        
        elif 'volume down' in query:
            User_commands.volume_down()
        
        elif 'mute' in query:
            User_commands.mute()
        
        elif 'weather' in query:
            User_commands.tell_weather()

        elif 'open youtube' in query:
            speak('Opening youtube')
            User_commands.open_youtube()

        elif 'open google' in query:
            speak('Opening Google')
            User_commands.open_google()

        elif 'time' in query:
            User_commands.tell_time()
        
        elif 'joke' in query:
            User_commands.tell_jokes()
        
        elif 'search' in query:
            User_commands.search_google()

        elif 'on youtube' in query:
            User_commands.play_youtube_video()

        elif 'open visual studio code' in query:
            User_commands.open_vscode()

        elif 'calculate' in query:
            User_commands.calculate()
        
        elif 'thank you' in query or 'thanks' in query:
            speak('My pleasure')

        elif 'bye' in query:
            speak('ok,boss bye bye!! ')
            exit()
        
        else:
            print('.....')
