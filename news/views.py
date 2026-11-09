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
 
    context = { 
        "articoli": Articles, 
        "giornalisti": Giornalisti 
    }
    
    print(context)
    return render(request, "news/homepage.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Article, pk=pk)
    context = {"articolo": articolo}
    return render(request, "news/articolo_detail.html", context)

def listaArticoli(request, pk=None):

    if pk is None:
        articoli = Article.objects.all()
        titolo_pagina = "Tutti gli articoli"
        giornalista_selezionato = None
    else:
        giornalista_selezionato = get_object_or_404(Giornalista, pk=pk)
        
        articoli = Article.objects.filter(giornalista=giornalista_selezionato)
        titolo_pagina = f"Articoli scritti da {giornalista_selezionato.nome} {giornalista_selezionato.cognome}"

    context = {
        'articoli': articoli,
        'titolo_pagina': titolo_pagina,
        'giornalista_selezionato': giornalista_selezionato,
    }

    return render(request, 'news/lista_articoli.html', context)