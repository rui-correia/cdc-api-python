from django.contrib import admin
from .models import Autor
from .models import Categoria

# Register your models here.
admin.site.register(Autor)
admin.site.register(Categoria)