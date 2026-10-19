from django.contrib import admin
from django.urls import path, include


from prova_pratica_1.views import somma
from prova_pratica_1.views import index
from prova_pratica_1.views import media

app_name="prova_pratica_1"

urlpatterns=[
    path('somma/', somma, name='somma'),
    path('media/', media, name = 'media'),
    path('admin/', admin.site.urls),
    path('index/', index, name = 'index')

]