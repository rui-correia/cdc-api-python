from rest_framework import serializers
from .models import Autor
from .models import Categoria


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ('name', 'email', 'descricao')


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nome',)
