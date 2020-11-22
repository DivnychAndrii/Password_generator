from django.shortcuts import render
import random


# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    the_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('123456789')
    special = list('!@#$%^&*()')

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])

    if request.GET.get('numbers'):
        characters.extend(numbers)

    if request.GET.get('special'):
        characters.extend(special)

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
