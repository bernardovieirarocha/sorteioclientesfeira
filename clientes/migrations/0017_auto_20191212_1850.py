# Generated by Django 2.2.1 on 2019-12-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_auto_20191212_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('FEMININO', 'Feminino'), ('MASCULINO', 'Masculino'), ('OUTRO', 'Outro')], max_length=9, null=True),
        ),
    ]
