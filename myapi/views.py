from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AutorSerializer
from .models import Autor

# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('name')
    serializer_class = AutorSerializer