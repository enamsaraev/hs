# Generated by Django 4.1.2 on 2023-01-07 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('mailing', '0002_alter_emailentry_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSendAutomaticly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.EmailField(help_text='Формат: обязательный', max_length=254, verbose_name='Почта для отправки смс покупателю')),
                ('subject', models.CharField(help_text='Формат: обязательный', max_length=255, verbose_name='Шапка смс для отправки почты покупателю')),
                ('text', models.TextField(help_text='Формат: обязательный', verbose_name='Текст смс для отправки почты покупателю')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, help_text='Формат: обязательный', verbose_name='Нажать, если нужно удалить шаблон')),
            ],
        ),
        migrations.AlterField(
            model_name='emailentry',
            name='email',
            field=models.CharField(help_text='Формат: обязательный', max_length=255, verbose_name='Почта клиента, оформившего и купившего товары (заказ)'),
        ),
        migrations.AlterField(
            model_name='emailentry',
            name='message',
            field=models.TextField(help_text='Формат: обязательный', verbose_name='Текст сообщения'),
        ),
        migrations.AlterField(
            model_name='emailentry',
            name='order',
            field=models.ForeignKey(blank=True, help_text='Формат: обязательный', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='emails', to='orders.order', verbose_name='Текущий заказ клиента'),
        ),
    ]
