# Generated by Django 4.0.1 on 2022-12-01 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0014_ip_remove_case_views_case_views'),
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
