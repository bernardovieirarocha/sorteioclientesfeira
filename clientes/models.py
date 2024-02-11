from django.db import models




class Person(models.Model):
    GENDER_CHOICES = (
        ("Feminino".upper(), "Feminino"),
        ("Masculino".upper(), "Masculino"),
        ("Outro".upper(), "Outro"),
    )

    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=9,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)

    @property
    def nome_completo(self):
        nome = str(self.first_name) + " " + str(self.last_name)
        return nome

    def __str__(self):
        return self.first_name







