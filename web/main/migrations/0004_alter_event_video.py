# Generated by Django 3.2.8 on 2021-11-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='video',
            field=models.FileField(blank=True, upload_to='videos/'),
        ),
    ]
