# Generated by Django 4.0.1 on 2022-12-01 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0020_remove_case_views_case_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='views',
        ),
        migrations.DeleteModel(
            name='Ip',
        ),
    ]
