# Generated by Django 5.1.1 on 2024-09-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('linkedin', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='InterpersonalSkill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('skill', models.CharField(max_length=10)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalExeperience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('campany_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('project_title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('technical_skills', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='projects_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('icons', models.ImageField(blank=True, null=True, upload_to='icons')),
            ],
        ),
    ]
