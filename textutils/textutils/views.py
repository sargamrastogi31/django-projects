from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Harry  Django CodeWithHarry</h1> <a href = "https://www.youtube.com/">Youtube</a>''')

# def about(request):
#     return HttpResponse("About Harry Bhai")

def index2(request):
    params={'name':'sargam','place':'gwalior'}
    return render(request, 'index2.html',params)

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if fullcaps=="on":
       analyzed=""
       for char in djtext:
         analyzed=analyzed+char.upper()
       params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
       djtext=analyzed
       #return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)
   
    # else:
    #       return HttpResponse("Error")
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
# before code
def removepunc(request):
     #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")

# def analyze(request):

#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     analyzed=djtext
#     params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
#     return render(request,'analyze.html',params)

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")

def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")

def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))