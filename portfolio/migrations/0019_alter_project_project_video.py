# Generated by Django 5.1.1 on 2024-10-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_alter_project_project_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_video',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]
