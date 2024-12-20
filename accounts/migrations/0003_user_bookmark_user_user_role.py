# Generated by Django 5.1.4 on 2024-12-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_verified'),
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_by', to='audio.audio'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('USER', 'User'), ('AUTHOR', 'Author'), ('ADMIN', 'Admin')], default='USER'),
        ),
    ]
