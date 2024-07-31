from django.shortcuts import render, redirect
from .models import Room, Message

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        room = request.POST["room"]
        try:
            Room.objects.get(room_name=room)
            return redirect('chat:room', room_name=room, username=username)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('chat:room', room_name=room, username=username)
    return render(request, 'chat_app/index.html') 

def MessageView(request, room_name, username):
    room = Room.objects.get(room_name=room_name)
    if request.method == "POST":
        message = request.POST["message"]
        new_message = Message(room=room, sender=username, message=message)
        new_message.save()
        
    messages = Message.objects.filter(room=room)   
    context = {
        "messages": messages,
        "user": username,
    } 
    return render(request, 'chat_app/message.html', context)