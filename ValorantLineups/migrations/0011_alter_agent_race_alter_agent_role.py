# Generated by Django 4.2 on 2023-04-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValorantLineups', '0010_agent_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='race',
            field=models.CharField(choices=[('Human', 'Human'), ('Radiant', 'Radiant'), ('Cybernetic', 'Cybernetic')], default='Unknown', max_length=30),
        ),
        migrations.AlterField(
            model_name='agent',
            name='role',
            field=models.CharField(choices=[('Controller', 'Controllers'), ('Duelist', 'Duelists'), ('Initiator', 'Initiators'), ('Sentinel', 'Sentinel')], default='Unknown', max_length=30),
        ),
    ]
