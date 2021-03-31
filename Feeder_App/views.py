from django.shortcuts import render
from django.http import HttpResponse

from .models import image, food

def index(request):
    pic_list = image.objects.all()
    return render(request, 'pic.html', {'pic_list': pic_list})

def message(request):
    message_list_unread = food.objects.filter(check_view=0).order_by('-notice_date')
    message_list_read = food.objects.filter(check_view=1).order_by('-notice_date')
    for message in message_list_unread:
        message.check_view = 1
        message.save()
    return render(request, 'message.html', {'message_list_unread': message_list_unread, 'message_list_read': message_list_read})
