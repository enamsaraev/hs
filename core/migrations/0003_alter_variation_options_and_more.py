# Generated by Django 4.1.2 on 2023-01-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_productinventory_media_media_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variation',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='variation',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='variation',
            name='color',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='size',
        ),
        migrations.AddField(
            model_name='variation',
            name='color',
            field=models.ManyToManyField(to='core.color'),
        ),
        migrations.AddField(
            model_name='variation',
            name='size',
            field=models.ManyToManyField(to='core.size'),
        ),
    ]