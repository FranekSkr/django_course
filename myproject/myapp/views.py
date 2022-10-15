from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': 'Franek',
        'age': 16,
        'surname': 'Skrobot'
    }
    return render(request, 'index.html', context)


def counter(request):
    words = request.GET['text']
    context = {
        'words': len(words.split())
    }
    return render(request, 'counter.html', context)
