from django.shortcuts import render
import random

def somma(request):

    context = {'var1': random.randint(1,10), 'var2' : random.randint(1,10)}

    somma = 'var1' + 'var2'

    return render(request, 'prova_pratica_1/somma.html', context, somma)


def media(request):

     lista1 = []

     for i in range(0,30):

           valore = random.randint(1,10)

           lista1.append(valore)

     return render (request, 'prova_pratica_1/media.html', lista1)

def index(request):
    
    return render(request, 'index.html')  

     




