# Generated by Django 5.1.3 on 2025-02-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackusers', '0002_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
