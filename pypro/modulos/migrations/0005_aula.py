# Generated by Django 4.1.5 on 2023-01-22 22:20 **

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0004_slug_unico_e_nao_nulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, null=True, verbose_name='order')),
                ('slug', models.SlugField(unique=True)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modulos.modulo')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
