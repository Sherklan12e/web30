# Generated by Django 5.0.2 on 2024-02-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='Imagenes/'),
        ),
    ]
