import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
import xlrd

def GTTS(text, filename):
    mytext = str(text)
    language = 'en'
    mydata = gTTS(text=mytext, lang= language, slow=True)
    mydata.save(filename)
    

def template():
    audio = AudioSegment.from_mp3('railway.mp3')
    # may i have you attension please
    start = 20000
    end = 22500
    audioprocess = audio[start:end]
    audioprocess.export("1_english.mp3", format='mp3')

    # from
    start = 122500
    end  =  123400
    audioprocess = audio[start:end]
    audioprocess.export("3_english.mp3", format='mp3')

    # to 
    start = 124000
    end  =  125000
    audioprocess = audio[start:end]
    audioprocess.export("5_english.mp3", format='mp3')

    # via
    start = 126000
    end  =  127000
    audioprocess = audio[start:end]
    audioprocess.export("7_english.mp3", format='mp3')

    # is arriving plateform number
    start = 129000
    end  =  132500
    audioprocess = audio[start:end]
    audioprocess.export("9_english.mp3", format='mp3')

def announcement(filename):
    df = xlrd.open_workbook(filename)
    print(df.sheet_by_index(0))
    

if __name__ == '__main__':
    print("starting")
    # template()
    announcement(r"C:\Users\Lenovo\PycharmProjects\railway annoouncement project\new_announce_hindi.csv")
    print('end')
        # Program to extract number
    # of rows using Python
    
    # Give the location of the file
    # loc = ("new_announce_english.csv")
    
    # wb = xlrd.open_workbook(loc)
    # sheet = wb.sheet_by_index(0)
    # sheet.cell_value(0, 0)
    
    # # Extracting number of rows
    # print(sheet.nrows)