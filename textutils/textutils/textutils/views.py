# This is created by me - Rishav

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello Rishav Bhai <a href = https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7> Django Project </a>")
#
# def about(request):
#     return HttpResponse("About Rishav Bhai")

def index(request):
    #params = {'name': 'Rishav' , 'place' : 'Pune'}
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('rem', 'off')
    print(djtext)
    print(removepunc)
    #analyzed = djtext
    punctuations = '''!()-_*&^%$##@!!~`.,\}{|'''
    analyzed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'punctuations removed', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
    #return HttpResponse("remo")  #always return a


# def capatalizefirst(request):
#     return HttpResponse("capatalizefirst")
#
# def spaceremove(request):
#     return HttpResponse("spaceremoe")



