from django.shortcuts import render
from django.http import HttpResponse
from .models import Produtos
def lista_de_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'lista_de_produtos.html', {'produtos': produtos})

def insert_product(request):
    nome = request.GET.get('nome')
    preco = request.GET.get('preco')
    descricao = request.GET.get('descricao')

    if nome and preco and descricao:
        produto = Produtos(nome=nome, preco=preco, descricao=descricao)
        produto.save()
        return HttpResponse(f'Produto {nome} inserido com sucesso!')
    return HttpResponse('Erro: Nome e Preço são obrigatórios!')

