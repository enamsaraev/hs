# Generated by Django 4.1.2 on 2023-07-23 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0012_alter_emailentry_is_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailsendautomaticly',
            name='recipient',
        ),
    ]