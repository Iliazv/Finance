# Generated by Django 4.0.1 on 2022-11-11 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0011_image_paragraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='image',
            field=models.ImageField(blank=True, upload_to='paragraph_images/'),
        ),
    ]
