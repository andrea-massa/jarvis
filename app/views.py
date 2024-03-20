from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    context = {'data': 'this is the data'}
    return render(request, 'homepage.html', context)    