# Generated by Django 4.0.1 on 2022-11-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0012_paragraph_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='title',
            field=models.CharField(max_length=350),
        ),
    ]
