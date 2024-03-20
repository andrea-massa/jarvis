from django.urls import path
from . import views

urlpatterns = [
    path('speech_to_text/', views.speech_to_text),
    path('text_to_speech/', views.text_to_speech),
    path('query_ai/', views.sendToChatGpt),
]