# Generated by Django 4.1.2 on 2023-07-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0011_emailsendautomaticly_email_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailentry',
            name='is_sent',
            field=models.BooleanField(default=True, verbose_name='Галочка стоит, если имейл доставлен'),
        ),
    ]
