from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

def index(request):
    return render(request,'index.html')

def random_word(request):
    request.session['word'] = get_random_string(length=14)
    counter = 0
    request.session['counter'] = counter + 1
    print(request.session.__dict__)
    return redirect('/show-word')

def show_word(request):
    return render(request, "rand-word.html")

def reset(request):
    counter = 0