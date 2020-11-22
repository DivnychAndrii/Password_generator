from django.shortcuts import render
import random


def home(request):

    the_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('123456789')
    special = list('!@#$%^&*()')

    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])

    if request.GET.get('numbers'):
        characters.extend(numbers)

    if request.GET.get('special'):
        characters.extend(special)

    length = int(request.GET.get('length', 12))
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/home.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')


