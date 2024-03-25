from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import json
import speech_recognition as sr

# Create your views here.



# An endpoint translating speech to text and returning JSON with the text 
def speech_to_text(request):    

    if request.method == "POST":

        # Access all the audio chunks in the request body 
        audio_chunks = request.FILES
        
        # Save the audio content in a single variable
        audio_content = b''        
        if len(audio_chunks) > 1:            
            for chunk in audio_chunks:
                audio_content += chunk.read()
        else:
            audio_content = audio_chunks['audioChunk_0']

        print(len(audio_content))

    return JsonResponse({'data': 'data'})



# An endpoint translating text to speech and returning AUDIO
def text_to_speech(request):
    return 'audio'



# An endpoint to send messages to ChatGPT
def sendToChatGpt(request):
    return 'txt'
    