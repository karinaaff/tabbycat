# Generated by Django 3.1.1 on 2020-09-02 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0010_auto_20190113_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailstatus',
            name='data',
            field=models.JSONField(blank=True, null=True, verbose_name='context'),
        ),
        migrations.AlterField(
            model_name='sentmessage',
            name='context',
            field=models.JSONField(blank=True, null=True, verbose_name='context'),
        ),
    ]
