from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import assemblyai as aai
import os

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

        # Format and send response
        return JsonResponse({'text': transcription})





# An endpoint translating text to speech and returning AUDIO
def text_to_speech(request):
    return 'audio'





# An endpoint to send messages to ChatGPT
def sendToChatGpt(request):
    return 'txt'
    








# ---------------------------HELPER FUNCTIONS ------------------------------------------

# A function that transcribes a .wav file to text using assemblyai API
def transcribe_file(filepath):
    # Set up the transcriber with aai
    aai.settings.api_key = os.environ.get('ASSEMBLY_AI_API_KEY')
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(filepath)

    # Handle errors in the transcription and return result
    if transcript.status == aai.TranscriptStatus.error:
        return('ERROR: '.format(transcript.error))
    else:
        return(transcript.text)