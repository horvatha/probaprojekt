from django.shortcuts import render

def index(request):
    context = {"idezetek": [
     "Nem esik messze",
     "Néma gyereknek az anyja se látja a fátol az erdőt.",
     "Áfásszámlaigényét kérjük előre jelezze",
     "A nyúlon túl.",
    ]}
    return render(request, "index.html", context)