from django.shortcuts import render
from anuncios.models import Anuncio
# Create your views here.
def anuncios(request):
    anuncios = Anuncio.objects.filter(status='publicado')
    return render(request,'anuncios/index.html',{'anuncios':anuncios})

def home(request):
    return render(request,"web/index.html")