# Generated by Django 2.2.1 on 2019-06-15 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('impostos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Person')),
                ('produtos', models.ManyToManyField(blank=True, to='clientes.Produto')),
            ],
        ),
    ]
