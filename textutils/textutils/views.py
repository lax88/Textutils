from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    removenew = request.POST.get('removenew','off')
    removespace = request.POST.get('removespace','off')
    charcount = request.POST.get('charcount','off')


    if (removepunc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_!`~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)
    
    if (removenew =="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed +char
        params = {'purpose':'Removed newline','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

        # return render(request, 'analyze.html', params)
    
    elif (removespace =="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed=analyzed +char
        params = {'purpose':'Removed Space','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

        # return render(request, 'analyze.html', params)

    elif (charcount =="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed +1
        params = {'purpose':'Character counted','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    
    if(removepunc!="on" and fullcaps!="on" and removenew !="on" and removespace !="on" and charcount !="on" ):
        return HttpResponse("<h1>Please select the operations!!</h1>")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html' )

def contactus(request):
    return render(request, 'contact.html')
