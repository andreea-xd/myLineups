# Generated by Django 4.2 on 2023-04-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValorantLineups', '0013_ability_ability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='race',
            field=models.CharField(choices=[('Human', 'Human'), ('Radiant', 'Radiant'), ('Cybernetic', 'Cybernetic')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='role',
            field=models.CharField(choices=[('Controller', 'Controllers'), ('Duelist', 'Duelists'), ('Initiator', 'Initiators'), ('Sentinel', 'Sentinel')], max_length=30, null=True),
        ),
    ]