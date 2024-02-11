from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
import datetime
from django.utils.timezone import utc
from django.views.generic.base import  TemplateView
from django.views import View
from clientes.models import Person
from django.db.models import *


def home(request):
    return render(request,'home_1.html')

def my_logout(request):
    logout(request)
    return redirect('home')


class DashboardView(View):

    def get(self,request):

            data = {
                'total_Person': Person.objects.all().aggregate(Count('id'))['id__count'],

                'gender_person_F':Person.objects.all().filter(gender='FEMININO').count(),
                'gender_person_M':Person.objects.filter(gender='MASCULINO').count(),
                'gender_person_O':Person.objects.all().filter(gender='OUTRO').count(),

                'media_idade': Person.objects.all().aggregate(Avg('age'))['age__avg'],
                'max_idade':Person.objects.all().aggregate(Max('age'))['age__max'],
                'min_idade':Person.objects.all().aggregate(Min('age'))['age__min'],

                'idade_0_18':Person.objects.all().filter(age__lte=18).count(),
                'idade_19_21':Person.objects.all().filter(age__gte=19).filter(age__lte=21).count(),
                'idade_21_60':Person.objects.all().filter(age__gte=22).filter(age__lte=60).count(),
                'idade_60_mais':Person.objects.all().filter(age__gte=61).count()


            }



            return render(request,'dashboard.html',{'my_data':data})

