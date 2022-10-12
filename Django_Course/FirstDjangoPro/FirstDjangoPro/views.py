# I have created this file - Keyur Chanchad
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')
    # return HttpResponse('<h1>Keyur</h1> <a href="www.google.com">Google</a>')

def BT_index(request):
    return render(request, 'BT_index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase', 'off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    newlineremove = request.POST.get('newlineremove','off')
    charcount = request.POST.get('charcount','off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if charcount == "on":
        count=0
        analyzed =""
        for char in djtext:
            count = count + 1
        analyzed += str(count)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}


    if (removepunc != "on" and newlineremove != "on" and extraspaceremove != "on" and uppercase != "on" and charcount != 'on'):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)





# def ex1(request):
#     sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#              ]
#     return HttpResponse((sites))