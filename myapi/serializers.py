from rest_framework import serializers
from .models import Autor

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ('name', 'email', 'descricao')