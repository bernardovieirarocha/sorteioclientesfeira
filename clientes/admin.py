from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais',{'fields':('first_name','last_name','age',)}),
        ('Dados complemtares',{"fields":('phone','gender','adress')}),
    )
    list_filter = ('age','gender')

    #fields = ('first_name','last_name','age','salary','doc','bio','photo')
    list_display = ('first_name','last_name','age','gender','phone','address')
    search_fields = ('id','first_name')


# Register your models here.
admin.site.register(Person,PersonAdmin)


