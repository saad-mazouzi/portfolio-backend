# Generated by Django 5.1.1 on 2024-10-01 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_interpersonalskill_skill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalexperience',
            name='project_video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
