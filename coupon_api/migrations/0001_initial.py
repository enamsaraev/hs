# Generated by Django 4.1.2 on 2023-01-15 16:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Формат: обязательный, макс. длины - 50 символов', max_length=50, unique=True, verbose_name='Код активации промокода')),
                ('valid_from', models.DateTimeField(help_text='Формат: обязательный', verbose_name='Дата начала действия промокода')),
                ('valid_to', models.DateTimeField(help_text='Формат: обязательный', verbose_name='Дата окончания действия промокода')),
                ('count', models.PositiveIntegerField(blank=True, help_text='Формат: необязательный', null=True, verbose_name='Количество использования промокода')),
                ('discount', models.PositiveIntegerField(help_text='Формат: обязательный, значение от 0%-100%', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='% скидки')),
                ('is_active', models.BooleanField(default=True, help_text='Формат: обязательный', verbose_name='Выбрать, если промокод используется')),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если промокод не используется')),
            ],
        ),
    ]
