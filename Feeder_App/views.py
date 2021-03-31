from django.shortcuts import render
from django.http import HttpResponse

from .models import image, food
import copy

def index(request):
    pic_list = image.objects.all()
    return render(request, 'pic.html', {'pic_list': pic_list})

def message(request):
    message_list_unread = food.objects.filter(check_view=False).order_by('-notice_date')
    message_list_read = food.objects.filter(check_view=True).order_by('-notice_date')
    message_list = copy.copy(message_list_read)
    print(message_list_read)
    for message in message_list_unread:
        message.check_view = True
        message.save()
    print(message_list)
    return render(request, 'message.html', {'message_list_unread': message_list_unread, 'message_list_read': message_list})
