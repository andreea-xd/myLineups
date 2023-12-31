# Generated by Django 4.2 on 2023-04-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValorantLineups', '0016_remove_video_side'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
