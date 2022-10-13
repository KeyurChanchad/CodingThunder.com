'''
What can this A.I. assistant do for you?
It can send emails on your behalf.
It can play music for you.
It can do Wikipedia searches for you.
It is capable of opening websites like Google, Youtube, etc., in a web browser.
It is capable of opening your code editor or IDE with a single voice command.
Enough talks! Let's start building our own J.A.R.V.I.S.

Defining Wish me Function :
Now, we will make a wishme() function that will make our J.A.R.V.I.S. wish or greet the user according to the time of computer or pc. To provide current or live time to A.I., we need to import a module called datetime. Import this module to your program by:

import datetime
Now, let's start defining the wishme() function:

def wishme():

hour = int(datetime.datetime.now().hour)

Here, we have stored the current hour or time integer value into a variable named hour. Now, we will use this hour value inside an if-else loop.

– Defining Take command Function :
The next most important thing for our A.I. assistant is that it should take command with the help of the microphone of the user's system. So, now we will make a takeCommand() function.  With the help of the takeCommand() function, our A.I. assistant will return a string output by taking microphone input from the user.

 Before defining the takeCommand() function, we need to install a module called speechRecognition. Install this module by:

pip install speechRecognition
After successfully installing this module, import this module into the program by writing an import statement.

import speechRecognition as sr

– Defining Task 5: To know the current time
  elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
In the above, code we are using the datetime() function and storing the current or live system time into a variable called strTime. After storing the time in strTime, we are passing this variable as an argument in speak function. Now, the time string will be converted into speech.

 Defining Task 6: To open the VS Code Program
 elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
To open the VS Code or any other application, we need the code path of the application

 Defining Speak Function
The first and foremost thing for an A.I. assistant is that it should be able to speak. To make our J.A.R.V.I.S. talk, we will make a function called speak(). This function will take audio as an argument, and then it will pronounce it.

def speak(audio):
       pass      #For now, we will write the conditions later.
Now, the next thing we need is audio. We must supply audio so that we can pronounce it using the speak() function we made. We are going to install a module called pyttsx3.

What is pyttsx3?
A python library that will help us to convert text to speech. In short, it is a text-to-speech library.
It works offline, and it is compatible with Python 2 as well as Python 3.
Installation:

pip install pyttsx3
In case you receive such errors:

No module named win32com.client
No module named win32
No module named win32api
Then, install pypiwin32 by typing the below command in the terminal :

pip install pypiwin32.
After successfully installing pyttsx3, import this module into your program.

import pyttsx3
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voice[0].id)

What is sapi5?
Microsoft developed speech API.
Helps in synthesis and recognition of voice.
What Is VoiceId?
Voice id helps us to select different voices.
voice[0].id = Male voice
voice[1].id = Female voice

Writing Our speak() Function :
We made a function called speak() at the starting of this tutorial. Now, we will write our speak() function to convert our text to speech.

def speak(audio):
engine.say(audio)
engine.runAndWait() #Without this command, speech will not be audible to us.

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    We have successfully created our takeCommand() function. Now we are going to add a try and except block to our program to handle errors effectively.

  try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")   #Say that again will be printed in case of improper voice
        return "None" #None string will be returned
    return query

Defining Task 1: To search something on Wikipedia
 To do Wikipedia searches, we need to install and import the Wikipedia module into our program. Type the below command to install the Wikipedia module :

pip install wikipedia
 After successfully installing the Wikipedia module, import it into the program by writing an import statement.

 if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

Defining Task 2: To open YouTube site in a web-browser
To open any website, we need to import a module called webbrowser. It is an in-built module, and we do not need to install it with a pip statement; we can directly import it into our program by writing an import statement.

Code:

     elif 'open youtube' in query:
            webbrowser.open("youtube.com")
Here, we are using an elif loop to check whether Youtube is in the user's query. Let' suppose the user gives a command as "J.A.R.V.I.S., open youtube." So, open youtube will be in the user's query, and the elif condition will be true.

32:34 – Defining Task 3: To open Google site in a web-browser
elif 'open google' in query:
            webbrowser.open("google.com")


 Defining Task 4: To play music
To play music, we need to import a module called os. Import this module directly with an import statement.

elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
In the above code, we first opened our music directory and then listed all the songs present in the directory with the os module's help. With the help of os.startfile, you can play any song of your choice. I am playing the first song in the directory. However, you can also play a random song with the help of a random module. Every time you command to play music, J.A.R.V.I.S. will play any random song from the song directory.

– Defining Task 7: To send Email
To send an email, we need to import a module called smtplib.

What is smtplib?

Simple Mail Transfer Protocol (SMTP) is a protocol that allows us to send emails and route emails between mail servers. An instance method called sendmail is present in the SMTP module. This instance method allows us to send an email.  It takes 3 parameters:
The sender: Email address of the sender.
The receiver: T Email of the receiver.
The message: A string message which needs to be sent to one or more than one recipient.

– Defining Send email function :
We will create a sendEmail() function, which will help us send emails to one or more than one recipient.

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
In the above code, we are using the SMTP module, which we have already discussed above.

 elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

Note: Do not forget to 'enable the less secure apps' feature in your Gmail account. Otherwise, the sendEmail function will not work properly.

'''

import pyttsx3   #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia    #pip install wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output


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
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('keyurchanchad21@gmail.com', 'keyur@job2020')
    server.sendmail('keyurchanchad21@gmail.com', to, content)     #server.sendmail(fromaddr, toaddrs, msg)
    server.close()   #server.quit()

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'G:\Audio\music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to keyur' in query:
            try:
                speak("What should You say?")
                content = takeCommand()
                to = "keyurchanchad@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend keyur bhai. I am not able to send this email")
