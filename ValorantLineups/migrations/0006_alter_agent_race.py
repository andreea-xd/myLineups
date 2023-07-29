# Generated by Django 4.2 on 2023-04-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValorantLineups', '0005_agent_description_agent_race_agent_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='race',
            field=models.CharField(choices=[('controllers', 'Controllers'), ('duelists', 'Duelists'), ('initiators', 'Initiators'), ('sentinels', 'Sentinel')], default='Unknown', max_length=30),
        ),
    ]