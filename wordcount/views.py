from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            # Increase
            wordDictionary[word] += 1
        else:
            # Add to the dictiionary
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'SortedwordDictionary': sortedWords})

def about(request):
    return render(request, 'about.html')
