from django.shortcuts import render

def esempio_if(request):
    dic = { 'var1': 200,
            'var2': 200,
            'var3': 300 }
    return render (request, "es_if.html", dic)

