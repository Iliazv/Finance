# Generated by Django 4.0.1 on 2022-12-01 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0018_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='views',
            field=models.OneToOneField(blank=True, default='0', on_delete=django.db.models.deletion.CASCADE, related_name='case_views', to='outsource.ip'),
        ),
    ]
