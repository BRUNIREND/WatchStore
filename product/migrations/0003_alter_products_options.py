# Generated by Django 5.0.2 on 2024-05-31 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_products_options_alter_products_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
