# Generated by Django 3.0.8 on 2020-07-15 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_campaign_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='budget',
            new_name='advertising_budget',
        ),
    ]
