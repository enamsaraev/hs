# Generated by Django 4.1.2 on 2023-03-11 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Купон', 'verbose_name_plural': 'Купоны'},
        ),
    ]
