from django.http import HttpResponse, response
from django.shortcuts import render, get_object_or_404
from .models import Article, Giornalista
import datetime

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

def queryBase(request):
    articoli_cognome = Article.objects.filter(giornalista__cognome='Rossi')
    
    numero_totale_articoli = Article.objects.count()

    try:
        giornalista_1 = Giornalista.objects.get(id=1)
        numero_articoli_giornalista_1 = Article.objects.filter(giornalista=giornalista_1).count()
    except Giornalista.DoesNotExist:
        giornalista_1 = None
        numero_articoli_giornalista_1 = 0

    articoli_ordinati = Article.objects.order_by('-visualizzazioni')

    articoli_senza_visualizzazioni = Article.objects.filter(visualizzazioni=0)

    articolo_piu_visualizzato = Article.objects.order_by('-visualizzazioni').first()

    giornalisti_data = Giornalista.objects.filter(data_nascita__gt=datetime.date(1990, 1, 1))

    articoli_del_giorno = Article.objects.filter(data_pubblicazione=datetime.date(2023, 1, 1))

    articoli_periodo = Article.objects.filter(data_pubblicazione__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))

    giornalisti_nati = Giornalista.objects.filter(data_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Article.objects.filter(giornalista__in=giornalisti_nati)

    giornalista_giovane = Giornalista.objects.order_by('-data_nascita').first()

    giornalista_anziano = Giornalista.objects.order_by('data_nascita').first()

    ultimi = Article.objects.order_by('-data_pubblicazione')[:5]

    articoli_minime_visualizzazioni = Article.objects.filter(visualizzazioni__gte=100)

    articoli_parola = Article.objects.filter(titolo__icontains='importante')

    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli': numero_totale_articoli,
        'giornalista_1': giornalista_1,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni': articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'articoli_giornalisti': articoli_giornalisti,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi': ultimi,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
    }

    return render(request, 'news/query.html', context)