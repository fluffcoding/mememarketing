# Generated by Django 3.0.8 on 2020-07-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
