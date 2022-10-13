import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)

# create speak function 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    speak('Hello sir, I am your Jarvis Desktop Assistant')
    # speak('All program are loaded in machin')
    