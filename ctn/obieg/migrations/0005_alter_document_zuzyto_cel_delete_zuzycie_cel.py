# Generated by Django 4.2 on 2023-04-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obieg', '0004_zuzycie_cel_document_data_dok_document_ksieg_ma1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='zuzyto_cel',
            field=models.CharField(choices=[(1, 'opcja1'), (2, 'opcja2'), (3, 'opcja3')], max_length=30),
        ),
        migrations.DeleteModel(
            name='Zuzycie_cel',
        ),
    ]
