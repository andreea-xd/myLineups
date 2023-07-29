# Generated by Django 4.2 on 2023-04-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValorantLineups', '0003_map_part_map_side'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='side',
        ),
        migrations.AddField(
            model_name='video',
            name='part',
            field=models.CharField(choices=[('all', 'All'), ('a', 'A'), ('b', 'B'), ('c', 'C')], default='all', max_length=10),
        ),
        migrations.AddField(
            model_name='video',
            name='side',
            field=models.CharField(choices=[('all', 'All'), ('attack', 'Attack'), ('defense', 'Defense')], default='all', max_length=10),
        ),
        migrations.AlterField(
            model_name='map',
            name='part',
            field=models.CharField(choices=[('a b', 'A B'), ('a b c', 'A B C')], max_length=50),
        ),
    ]
