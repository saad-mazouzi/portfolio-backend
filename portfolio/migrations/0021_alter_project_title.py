# Generated by Django 5.1.1 on 2024-10-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_rename_project_video_project_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
