# Generated by Django 4.1.2 on 2023-03-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderitems',
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='order',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Выбрать, если заказ должен быть удален'),
        ),
    ]