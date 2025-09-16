from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from contatos.models import Pessoa
from contatos.forms import ContatosModel2Form


class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all().order_by('nome')
        contexto = {'pessoas': pessoas}
        return render(request, 'contatos/listaContatos.html', contexto)


class ContatoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'formulario': ContatosModel2Form}
        return render(request, 'contatos/criaContato.html', contexto)

    def post(self, request, *args, **kwargs):
        formulario = ContatosModel2Form(request.POST)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(
                reverse_lazy('contatos:lista-contatos')
            )


class ContatoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        formulario = ContatosModel2Form(instance=pessoa)
        context = {'pessoa': formulario}
        return render(request, 'contatos/atualizaContatos.html', context)

    def post(self, request, pk, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ContatosModel2Form(request.POST, instance=pessoa)
        if formulario.is_valid():
            pessoa = formulario.save()
            pessoa.save()
            return HttpResponseRedirect(
                reverse_lazy('contatos:lista-contatos')
            )
        else:
            context = {'pessoa': formulario}
            return render(request, 'contatos/atualizaContatos.html', context)
