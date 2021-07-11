from django.shortcuts import render
from Portfolio import models
# Create your views here.
def portfolio(request):
    portfolios = models.Image.objects.filter(status='activa')
    return render(request,'portfolio/index.html',{"portfolios":portfolios})