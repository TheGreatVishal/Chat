from django.shortcuts import render,redirect,HttpResponse
from . import friends_lib as fl
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def get_users(request):

    db = fl.Database()
    username = (request.GET["username"])

    all_user_list = []
    final_list = []
    
    all_user_list = db.all_users()
    db.close()
    
    
    for user in all_user_list:
        if(username != ""):
            if(username == user[0:len(username)]):
                final_list.append(user)
        else:
            break
    
    
    return JsonResponse({"user_list" : final_list})

def friend(request):
    
    db = fl.Database()
    
    try :
        db.create_table_of_friends(str(request.user))
    except:
        pass

    try :
        db.create_table_of_requests(str(request.user))
    except:
        pass
    
    friends = db.retrieve_friends(str(request.user))
    db.close()
    
    friend = sorted(friends, key=lambda x: (ord(x.lower()[0]), x.lower()))

    return render(request,"friends.html",{"friends" : friend})


def requests(request):
    
    db = fl.Database()
    
    try :
        db.create_table_of_friends(str(request.user))
    except:
        pass

    try :
        db.create_table_of_requests(str(request.user))
    except:
        pass
    
    requests = db.retrieve_requests(str(request.user))
    db.close()
   
    return render(request,"requests.html",{"requests" : requests})


def accept(request, source_user):
    
    db = fl.Database()
   
    receiver = str(request.user)
    sender = source_user
   
    db.friendship(sender, receiver)
   
    db.close
    return redirect("requests")

def reject(request, source_user):
    
    db = fl.Database()
    
    receiver = str(request.user)
    sender = source_user
    
    db.reject_friend_request(sender, receiver)
    
    db.close
    return redirect("requests")


def add_friend(request):
    
    return render(request, "add_friend.html")

def send_request(request):

    if(request.method == "POST"):
       
        db = fl.Database()
        
        username = request.POST["username"]  # username of person to whom we are sending request
        
        try : 
            db.create_table_of_friends(username)
        except:
            pass
        
        try : 
            db.create_table_of_requests(username)
        except:
            pass
        
        if(db.if_username_exists(username)):
            
            if(username == str(request.user)):
               
                messages.info(request, "Can't send request to Yourself!")
                db.close()
                return redirect("add_friend")
            
            elif(db.if_request_already_sent(str(request.user), username)):
                
                messages.info(request, "Friend request already sent!")
                db.close()
                return redirect("add_friend")
            
            elif(db.if_already_friends(str(request.user), username)):
                
                messages.info(request, "You are already friends!")
                db.close()
                return redirect("add_friend")
            
            elif(db.if_friend_request_exist(str(request.user), username)):
                
                messages.info(request, "You already have Friend Request from this person !")
                db.close()
                return redirect("add_friend")
            
            else:
                
                db.send_friend_request(str(request.user), username)
                messages.info(request, "Request sent!")
                db.close()
                return redirect("add_friend")

        else:
            
            messages.info(request, "User not found!")
            db.close()
            return redirect("add_friend")
            
    else:
        
        return redirect(request, "add_friend.html")
    
def remove(request, target):
    
    database = fl.Database()
    
    user = str(request.user)
    database.end_friendship(user, target)

    database.close()
    return redirect("friend")