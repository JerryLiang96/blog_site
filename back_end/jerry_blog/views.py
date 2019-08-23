from django.shortcuts import render

context = {}

def home(request):
    context['text'] = 'Welcome!'
    return render(request, 'home.html', context)