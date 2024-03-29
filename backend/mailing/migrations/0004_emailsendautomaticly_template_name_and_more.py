# Generated by Django 4.1.2 on 2023-03-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_remove_emailentry_message_emailentry_from_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsendautomaticly',
            name='template_name',
            field=models.CharField(blank=True, help_text='Название шаблона', max_length=255, null=True, verbose_name='Имя шаблона письма'),
        ),
        migrations.AlterField(
            model_name='emailentry',
            name='email',
            field=models.EmailField(help_text='Обязательный, принимать ТОЛЬКО имейл', max_length=200, verbose_name='Получать сообщения'),
        ),
        migrations.AlterField(
            model_name='emailentry',
            name='from_email',
            field=models.EmailField(default='', help_text='Обязательный, по дефолту хранит хоста от почты', max_length=200, verbose_name='Отправитель сообщения'),
        ),
        migrations.AlterField(
            model_name='emailentry',
            name='subject',
            field=models.CharField(help_text='Обязательный, принимает текст', max_length=255, verbose_name='Тема сообщения'),
        ),
        migrations.AlterField(
            model_name='emailentry',
            name='template_name',
            field=models.CharField(blank=True, help_text='Название шаблона', max_length=255, null=True, verbose_name='Имя шаблона письма'),
        ),
        migrations.AlterField(
            model_name='emailentry',
            name='text',
            field=models.TextField(blank=True, help_text='Обязательный, принимает текст', null=True, verbose_name='Текст письма'),
        ),
    ]
