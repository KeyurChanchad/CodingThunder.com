from bs4 import BeautifulSoup
from main import notifyMe
from plyer import notification # pip install plyer or winnotify
import requests

def notifyme(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'C:\\Users\\Lenovo\\PycharmProjects\\covidNotify\\icon.ico',
        timeout = 5
    )

if __name__ == '__main__':from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Lenovo\\PycharmProjects\\covidNotify\\icon.ico",
        timeout = 6
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        # notifyMe("Harry", "Lets stop the spread of this virus together")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tbody in soup.find_all('tbody'):   
             for tr in tbody:
                 print(tr)
        print(myDataStr)
        
        # for tr in soup.find_all('tbody'):
            # myDataStr += tr
        # print(myDataStr)
        # myDataStr = myDataStr[1:]
        # itemList = myDataStr.split("\n\n")

        # states = ['Chandigarh', 'Telengana', 'Uttar Pradesh']
        # for item in itemList[0:22]:
        #     dataList = item.split('\n')
        #     if dataList[1] in states: 
        #         nTitle = 'Cases of Covid-19'
        #         nText = f"State {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured :  {dataList[4]}\nDeaths :  {dataList[5]}"
        #         notifyMe(nTitle, nText)
        #         time.sleep(2)
        # time.sleep(5)       
    
    


