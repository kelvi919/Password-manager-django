from django.shortcuts import render
from django.http import HttpResponse
import random

import generator

def home(request):
    return render(request, "generator/home.html")


def password(request):
    """check if uppercase, spezial, and numbers should go into the password"""
    charackters = list("abcdefghijklmnopqrstuvwxyz")
    charackters_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("123456789")
    spezial = list("!£$%^&*()_-")

    if request.GET.get("uppercase"):
        charackters.extend(charackters_upper)
    if request.GET.get("numbers"):
        charackters.extend(numbers)
    if request.GET.get("special"):
        charackters.extend(spezial)

    length = int(request.GET.get("length", 12))
    gen_password = ""

    for i in range(length):
        gen_password += random.choice(charackters)
    return render(request, "generator/password.html", {"password": gen_password})
