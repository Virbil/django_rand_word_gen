from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

def index(request):
    request.session['counter']
    return render(request,'index.html')

def random_word(request):
    request.session['word'] = get_random_string(length=14)
    request.session['counter'] += 1
    return redirect('/show-word')

def show_word(request):
    return render(request, "rand-word.html")

def reset(request):
    request.session['counter'] = 0
    return redirect('/')