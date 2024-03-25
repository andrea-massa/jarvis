from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import json
import tempfile
import os
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
            print(type(audio_chunks['audioChunk_0']))
            audio_content = audio_chunks['audioChunk_0'].read()
        

        # Save audio into a temporary WAV file
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio_file:
            temp_audio_file.write(audio_content)
            temp_audio_file_path = temp_audio_file.name

        

    return JsonResponse({'data': 'data'})



# An endpoint translating text to speech and returning AUDIO
def text_to_speech(request):
    return 'audio'



# An endpoint to send messages to ChatGPT
def sendToChatGpt(request):
    return 'txt'
    