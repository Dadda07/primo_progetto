from django.http import HttpResponse, response
from django.shortcuts import render, get_object_or_404
from .models import Article, Giornalista

'''
def home(request): 

    a = "" 
    g = ""

    for art in Article.objects.all():
        a+= (art.titolo + "<br>")

    for gior in Giornalista.objects.all():
        g+= (gior.nome +  "<br>")

    response = "Artioli: <br>" + a + "<br>Giornalisti: <br>" + g

    return HttpResponse("<h1>" + response + "</h1>")

'''

'''
def home(request):
    a = []
    b = []

    for art in Article.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        b.append(gio.nome)

    response = str(a) + "<br>" + str(b)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")

 '''

def home(request):
    Articles = Article.objects.all()
    Giornalisti = Giornalista.objects.all()
    context = { "Articles": Articles, "Giornalisti": Giornalisti }
    print(context)
    return render(request, "news/home.html", context)

def articoloDetailView(request, pk):
    # articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Article, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)