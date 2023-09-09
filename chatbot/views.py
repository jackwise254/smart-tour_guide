from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(['POST'])
def chatbot_response(request):
    user_message = request.data.get('message', '')
    bot_message = get_bot_response(user_message)
    
    return Response({"response": bot_message})


def get_bot_response(user_message):
    # Placeholder logic: You can integrate more advanced chatbot functionalities here.
    if "hello" in user_message.lower():
        return "Hi there!"
    return "I'm not sure how to respond to that."

from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({"detail": "CSRF cookie set"})
