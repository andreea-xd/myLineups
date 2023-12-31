# Generated by Django 4.2 on 2023-04-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValorantLineups', '0014_alter_agent_race_alter_agent_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='type',
            field=models.CharField(choices=[('setup', 'Setup'), ('lineup', 'Lineup'), ('mechanics', 'Mechanics')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ability',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='part',
            field=models.CharField(choices=[('all', 'All'), ('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='side',
            field=models.CharField(choices=[('all', 'All'), ('attack', 'Attack'), ('defense', 'Defense')], max_length=10, null=True),
        ),
    ]
