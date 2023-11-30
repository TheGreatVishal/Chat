from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from . import chat_lib 
import Friends.friends_lib as fl

# Create your views here.

def chat(request):        
    
    return render(request, "chat.html")

# fetch messages of general chat
def get_messages(request):
    
    database = chat_lib.Database()
    
    message_list = database.pull()
    messages = [message[0] for message in message_list]

    database.close()
    return JsonResponse({"messages" : messages})

# fetching messages from particular table
def get_messages_dm(request, message_table):
    
    database = chat_lib.Database()
        
    message_list = database.pull_dm(message_table)
    messages = [message[0] for message in message_list]

    database.close()
    return JsonResponse({"messages" : messages})
        
def put_message(request):
    
    database = chat_lib.Database()
    
    message = request.POST["message"]
    if(len(message) > 0):
        message = str(request.user) + " : " + message
        database.push(message)
    database.close()
    return HttpResponse()

def put_messages_dm(request, message_table):
    
    database = chat_lib.Database()
    
    message = request.POST["message"]
    if(len(message) > 0):
        message = str(request.user) + " : " + message
        database.push_dm(message, message_table)
    database.close()
    return HttpResponse()

def reset_chat(request):
    
    database = chat_lib.Database()
    database.reset_chat()
    database.close()
    return render(request, "chat.html")

def reset_chat_dm(request, message_table, name):
    
    database = chat_lib.Database()
    database.reset_chat_dm(message_table)
    database.close()
    
    return redirect(f"/Chat/dm/{name}")
    
def direct_chat(request):
    
    db = fl.Database()
    friends = db.retrieve_friends(str(request.user))
    db.close()
    
    return render(request,"direct_chat.html",{"friends" : friends})


def dm(request, receiver):

    db = chat_lib.Database()
    
    sender = str(request.user)
    
    if (sender <= receiver) :
        smaller = sender
        bigger = receiver
    else :
        smaller = receiver
        bigger = sender
    
    message_table = "messages_of_" + smaller + "_" + bigger
        
    try :
        db.create_table(message_table)
    except :
        pass
    
    return render(request,"dm.html",{"name" : receiver, "message_table" : message_table})