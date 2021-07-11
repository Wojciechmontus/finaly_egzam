from django.shortcuts import render
from empresa.models import Empresa
# Create your views here.
def mostrarEmpresa(request):
    contentBussines = Empresa.objects.all()
    return render(request,'empresa/index.html',{'empresas':contentBussines})