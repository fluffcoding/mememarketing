# Generated by Django 3.0.8 on 2020-07-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0006_auto_20200717_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignexecutionunit',
            name='social_media_platform',
            field=models.CharField(choices=[('t', 'twitter'), ('i', 'instagram'), ('y', 'youtube'), ('f', 'facebook')], max_length=50),
        ),
        migrations.AlterField(
            model_name='socialmediaasset',
            name='platform',
            field=models.CharField(choices=[('t', 'twitter'), ('i', 'instagram'), ('y', 'youtube'), ('f', 'facebook')], max_length=20),
        ),
    ]
