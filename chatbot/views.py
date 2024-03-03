from dotenv import load_dotenv
import os
from openai import OpenAI
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse 

# Create your views here.

def getCompletion(prompt):
    client = OpenAI(
        api_key = os.getenv("OPENAI_KEY_3"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    res = chat_completion.choices[0].message.content
    return res 


@api_view(['POST'])
def PostChatBot(request):
    if request.method == 'POST': 
        prompt = request.POST.get('prompt') 
        result = getCompletion(prompt) 
        return Response(result)  