from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import json
import tempfile
import os
import speech_recognition as sr

# Create your views here.



# An endpoint translating speech to text and returning JSON with the text 
def speech_to_text(request):    


    def transcribe_file(filepath):

        try:
            r = sr.Recognizer()                            
            with sr.AudioFile(filepath) as source:
                audio = r.record(source)
                result = r.recognize_google(audio)
                return result

        except sr.UnknownValueError:
            return 'ERROR: Could Not Understand Audio'
        except sr.RequestError as e:
            return 'ERROR: {error}'.format(e)


    if request.method == "POST":

        # Access all the audio chunks in the request body 
        audio_chunks = request.FILES
        
        # Save the audio content in a single variable
        audio_content = b''        
        if len(audio_chunks) > 1:            
            for chunk in audio_chunks:                
                audio_content += chunk.read()
        else:
            audio_content = audio_chunks['audioChunk_0'].read()

        # Create a directory to save audio chunk to a file
        save_dir = './api/temp_audio_files/'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        # Save audio to file in that directory
        save_path = os.path.join(save_dir, 'audio.wav')
        print('Save Path: ', save_path)
        with open(save_path, 'wb') as f:
            f.write(audio_content)

        # Transcribe the file to text
        transcription = transcribe_file(save_path)

    return JsonResponse({'data': 'data'})



# An endpoint translating text to speech and returning AUDIO
def text_to_speech(request):
    return 'audio'



# An endpoint to send messages to ChatGPT
def sendToChatGpt(request):
    return 'txt'
    