from django.shortcuts import render
import json
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

TOKEN = "TOKENX"

@csrf_exempt
def chatbotRoutes(request):
    if request.method == "GET":
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")
        mode = request.GET.get('hub.mode')
        if mode == 'subscribe' and token == TOKEN:
            return HttpResponse(challenge or '', status=200)
        else:
            return HttpResponse('Verification failed', status=403)
    elif request.method == "POST":
        #return HttpResponse('Verification good', status=201)
        response = engineEntry(request) 
        return response
    
def engineEntry(req):
    try:
        data = json.loads(req.body.decode('utf-8'))
        msg_object = data.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {}).get("messages", [])
        
        if msg_object:
                messages = msg_object[0]

                if "type" in messages:
                    type_ = messages["type"]
                    
                    if type_ == "interactive":
                        interactive_type = messages["interactive"]["type"]

                        if interactive_type == "button_reply":
                            content = messages["interactive"]["button_reply"]["id"]
                            phone_number = messages["from"]
                            
                        elif interactive_type == "list_reply":
                            content = messages["interactive"]["list_reply"]["id"]
                            phone_number = messages["from"]
                            
                    if type_ == "text":
                        content = messages["text"]["body"]
                        phone_number = messages["from"]     
        
        return HttpResponse(status=200)
    except ValueError:
        return HttpResponse(status=400) # invalid JSON
    