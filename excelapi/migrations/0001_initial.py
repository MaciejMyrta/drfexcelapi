# Generated by Django 3.2.6 on 2021-08-11 09:26

import django.core.validators
from django.db import migrations, models
import excelapi.models
import excelapi.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=excelapi.models.fileName, validators=[django.core.validators.FileExtensionValidator(['xlsx']), excelapi.validators.validate_size])),
                ('columns', models.CharField(max_length=255)),
            ],
        ),
    ]
