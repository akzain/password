from django.shortcuts import render
from django.http import HttpResponse
from random import choice

# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("special"):
        characters.extend(("!@#$%^&*()<>?:;|\}{[]"))
    
    if request.GET.get("numbers"):
        characters.extend(("1234567890"))

    length = int(request.GET.get("length", 12))
    password = ""

    for x in range(length):
        password += choice(characters)
    context = {"password": password}
    return render(request, "generator/password.html", context)

def about(request):
    return render(request, 'generator/about.html')

