# Generated by Django 4.2.5 on 2023-10-03 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
