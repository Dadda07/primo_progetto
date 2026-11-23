from django.urls import path
from .views import home, articoloDetailView, listaArticoli, queryBase, giornalistaDetailView, articoloDetailView

app_name = "news"

urlpatterns = [
    path('', home, name='homeview'), 
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path('lista_articoli/', listaArticoli, name='lista_articoli'),
    path('query/', queryBase, name='query'),
    path('lista_articoli/<int:pk>/', listaArticoli, name='lista_articoli_giornalista'),
    path('articoli/<int:pk>', articoloDetailView, name='articolo_detail'),
    path('giornalisti/<int:pk>', giornalistaDetailView, name='giornalista_detail')

]