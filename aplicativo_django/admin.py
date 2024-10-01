from django.contrib import admin
from .models import Produtos
class ProdutosAdmin(admin.ModelAdmin):
    lista = ('nome  ', 'preco', 'descricao')
admin.site.register(Produtos)


# Register your models here.
