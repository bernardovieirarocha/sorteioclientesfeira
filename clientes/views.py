from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Person
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Person
import random
from django.db.models import *
import os

#Cbv Person

@login_required
def sorteio(request):
    persons= Person.objects.all()
    lista_pessoas = []

    for pessoa in persons:
        lista_pessoas.append(pessoa.id)

    index = random.randint(0,len(lista_pessoas)-1)

    id_sorteado = lista_pessoas[index]

    sorteado = Person.objects.get(pk=id_sorteado)

    return render(request,'sorteio.html',{'sorteado':sorteado})

class PersonList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Person
    permission_required = ("clientes.view_person")

    def  get_queryset(self):
        termo_busca = self.request.GET.get('pesquisa' , None)

        if termo_busca:
            persons =Person.objects.filter(first_name__icontains=termo_busca)
        else:
            persons = Person.objects.all().order_by('first_name')

        return persons




class PersonDetail(LoginRequiredMixin,DetailView):
    model = Person

    def get_success_url(self):
        return  reverse_lazy('person_list_cbv')




class PersonCreate(LoginRequiredMixin,CreateView):
    model = Person
    fields = ['first_name','last_name',"age","gender","phone",'address']



    def get_success_url(self):
        return  reverse_lazy('person_list_cbv')
        

class PersonUpdate(LoginRequiredMixin,UpdateView):
    model = Person
    fields = ['first_name','last_name',"age","gender","phone",'address']
    #success_url = reverse_lazy('person_list_cbv')


    def get_success_url(self):
        return  reverse_lazy('person_list_cbv')

class PersonDelete(LoginRequiredMixin,DeleteView):
    model = Person
    #success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return  reverse_lazy('person_list_cbv')



