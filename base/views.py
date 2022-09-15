from django.shortcuts import render, redirect
import urllib.request
import json


def home(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
        try:
            data = urllib.request.urlopen(url).read()
            js = json.loads(data)
            meanings = js[0]['meanings']
            
            context = {'meanings': meanings , 'word': word.upper()}
            return render(request, 'main.html', context )
        except:
                context = {'word': word.upper}
                return render(request, 'main.html', context )
           
    return render(request, 'main.html')