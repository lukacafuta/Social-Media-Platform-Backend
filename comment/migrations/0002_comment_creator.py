# Generated by Django 5.0.6 on 2024-06-19 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
        ('userProfile', '0002_alter_userprofile_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='userProfile.userprofile'),
        ),
    ]
