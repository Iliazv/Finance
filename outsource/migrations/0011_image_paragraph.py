# Generated by Django 4.0.1 on 2022-11-11 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0010_remove_image_paragraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='paragraph',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='outsource.paragraph'),
        ),
    ]
