from django.shortcuts import render
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
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
