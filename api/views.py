from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

# Create your views here.

# An endpoint translating speech to text and returning JSON with the text 
def speech_to_text(request):    
    return 'txt'

# An endpoint translating text to speech and returning AUDIO
def text_to_speech(request):
    return 'audio'

# An endpoint to send messages to ChatGPT
def sendToChatGpt(request):
    return 'txt'
    