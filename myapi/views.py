from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AutorSerializer
from .serializers import CategoriaSerializer
from .models import Autor
from .models import Categoria

# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('name')
    serializer_class = AutorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nome')
    serializer_class = CategoriaSerializer