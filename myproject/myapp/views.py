from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about1(request):
    return render(request, 'about1.html')


def about2(request):
    return render(request, 'about2.html')


def go1(request):
    return render(request, 'go1.html')


def go2(request):
    return render(request, 'go2.html')
    

def result1(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words: 
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request, 'result1.html', {'full': text, 'total': len(words), 'dictionary' : word_dictionary.items()})


def result2(request):
    text = request.GET['fulltext']
    words = list(text)
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result2.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})

