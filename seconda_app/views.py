from django.shortcuts import render


def es_if(request):
    dic = { 'var1': 200,
            'var2': 200,
            'var3': 300 }
    return render (request, "seconda_app/es_if.html", dic)

def if_else_elif(request):
    dic = {    'var1': 120,
                'var2': 200,
                'var3': 300 }
    return render (request, "seconda_app/if_else_elif.html", dic)

def es_for(request):
    dic = {'list1' : [1, 2, 3, 4, 5] , 'list2':[ 6, 7, 8, 9, 10]}

    return render(request, "seconda_app/es_for.html", dic)
