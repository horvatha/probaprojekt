from django.shortcuts import render
import random


def index(request):
    idezetek = [
        "Nem esik messze",
        "Néma gyereknek az anyja se látja a fátol az erdőt.",
        "Áfásszámlaigényét kérjük előre jelezze",
        "A nyúlon túl.",
    ] * 8
    context = {
        "idezetek": idezetek,
        "veletlen_idezet": random.choice(idezetek)
    }
    return render(request, "index.html", context)