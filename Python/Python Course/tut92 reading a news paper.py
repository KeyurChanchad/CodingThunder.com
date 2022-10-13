
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url= "https://newsapi.org/v2/top-headlines?country=in&apiKey=11d27f6291bc49909dca4bfaa4da1054"
    news = requests.get(url).text
    py_dic = json.loads(news)   # josn.loads take str
    arts = py_dic["articles"]
    for articles in arts:
        speak(articles["title"])
        speak("Moving on to the next news..Listen Carefully")

speak("Thanks for listening...")





