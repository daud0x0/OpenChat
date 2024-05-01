from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
import json


import google.generativeai as genai
import os



from .models import Character, Category

# Create your views here.

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-pro-latest')


def search(request):
    query = request.GET.get('q', '')
    characters = Character.objects.filter().filter(Q(description__icontains=query))

    return render(request, 'chat/search.html', {
        'query': query,
        'characters': characters,
    })




def home(request):
    return render(request, 'chat/home.html',{
        "characters":Character.objects.all()
    })

# Create your views here.

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def about(requests):
    return render(requests, 'chat/about.html')


def home(request):
    return render(request, 'chat/home.html',{
        "characters":Character.objects.all()
    })

def chat_with_character(requests, category_slug, character_slug):
    category = get_object_or_404(Category, slug=category_slug)
    character = get_object_or_404(Character, category=category, slug=character_slug)
    if requests.method == 'POST':
        
      try:
        user_chat = requests.body.decode('utf-8')
        user_chat = json.loads(user_chat).get('message', '')
        model = genai.GenerativeModel('gemini-1.5-pro-latest', system_instruction=character.prompt_instruction)
        chat = model.start_chat(history=[])
        response = chat.send_message(user_chat)
        
        character_chat = {'message': response.text}

        return JsonResponse(character_chat, status=200)

      except json.JSONDecodeError as e:
            # Handle JSON decoding error
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return render(requests, 'chat/character_chat.html', {'character': character})
    
    
