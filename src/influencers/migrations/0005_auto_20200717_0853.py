# Generated by Django 3.0.8 on 2020-07-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0004_auto_20200717_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignexecutionunit',
            name='social_media_platform',
            field=models.CharField(choices=[('y', 'youtube'), ('f', 'facebook'), ('t', 'twitter'), ('i', 'instagram')], max_length=50),
        ),
        migrations.AlterField(
            model_name='socialmediaasset',
            name='platform',
            field=models.CharField(choices=[('y', 'youtube'), ('f', 'facebook'), ('t', 'twitter'), ('i', 'instagram')], max_length=20),
        ),
    ]
