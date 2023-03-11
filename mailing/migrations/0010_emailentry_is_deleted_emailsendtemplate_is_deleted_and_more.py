# Generated by Django 4.1.2 on 2023-03-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0009_rename_template_name_emailsendautomaticly_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailentry',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Выбрать, если запись должна быть удалена'),
        ),
        migrations.AddField(
            model_name='emailsendtemplate',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Выбрать, если запись должна быть удалена'),
        ),
        migrations.AlterField(
            model_name='emailsendautomaticly',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Выбрать, если запись должна быть удалена'),
        ),
    ]
