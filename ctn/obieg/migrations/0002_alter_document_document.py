# Generated by Django 4.1.7 on 2023-04-03 03:33

from django.db import migrations, models
import obieg.models


class Migration(migrations.Migration):

    dependencies = [
        ('obieg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=obieg.models.user_directory_path),
        ),
    ]
