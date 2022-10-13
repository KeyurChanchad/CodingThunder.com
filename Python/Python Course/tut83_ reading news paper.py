"""
# Akhbaar padhke sunaao
# Attempt it yourself and watch the series for solution and shoutouts for this lecture!

# import pynin32
"""
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
     # speak("Hello sir , I am your jarvis desktop computer. All system is working fine ");
     speak("Keyur sir, All System is working fine and all program is load to machine")
     


# import newsapi-python

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient()

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                              sources='bbc-news,the-verge',
                                              category='business',
                                              language='en',
                                              country='us')
speak(top_headlines)
print("Top Headlines ", top_headlines)
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          domains='bbc.co.uk,techcrunch.com',
                                          from_param='2017-12-01',
                                          to='2017-12-12',
                                          language='en',
                                          sort_by='relevancy',
                                          page=2)

print("All articles ", all_articles)

# /v2/sources
sources = newsapi.get_sources()

print("source ", sources)
