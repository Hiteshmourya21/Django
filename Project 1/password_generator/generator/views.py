from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request , 'generator\home.html' )

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    lenght = int(request.GET.get('length' , 12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request , 'generator\password.html' , {'password' : thepassword})

def about(request):
    return render(request , 'generator/about.html' )