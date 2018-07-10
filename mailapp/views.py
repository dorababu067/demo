from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    send_mail('confiramtion','hellow this is send my dorababu',
    'dorababua77@gmail.com',['cdevendra7@gmail.com'],fail_silently=False)
    return render(request,"index.html")
