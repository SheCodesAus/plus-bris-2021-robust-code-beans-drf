# Generated by Django 3.2.5 on 2021-11-15 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_profile_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default='2021-09-25T00:28:23.382748+10:00'),
            preserve_default=False,
        ),
    ]