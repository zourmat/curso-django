# Generated by Django 4.1.5 on 2023-01-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_propulando_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]