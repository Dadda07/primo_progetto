
from django.contrib import admin
from django.urls import path, include


from prima_app.views import homepage
from prima_app.views import welcome
from prima_app.views import lista
from prima_app.views import chi_siamo
from prima_app.views import variabili
from prima_app.viws import index

app_name="prima_app"

urlpatterns=[

    path('', homepage, name='homepage'),
    path('welcome/', welcome, name='welcome'),
    path('lista/', lista, name='lista'),
    path('chi_siamo/', chi_siamo, name = 'chi_siamo'),
    path('variabili/', variabili, name = 'variabili')
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', include('prima_app.urls'))

]