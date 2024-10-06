from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key = True)
    email = models.CharField(max_length = 255)
    linkedin = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)


    def __str__(self) :
        return self.email

class AboutMe(models.Model):
    id  = models.AutoField(primary_key = True)
    profile_picture = models.ImageField(upload_to = 'profile_pictures/')
    description = models.TextField()
    
    class Meta:
        verbose_name_plural="About me"

    

class ProfessionalExperience(models.Model):
    id = models.AutoField(primary_key = True)
    company_logo = models.ImageField(upload_to='company_logos/') 
    campany_name = models.CharField(max_length = 50)
    job_title = models.CharField(max_length = 255)
    start_date = models.DateField()
    end_date = models.DateField()
    project_title = models.TextField()
    description = models.TextField()
    technical_skills = models.CharField(max_length = 255)
    location = models.CharField(max_length = 50)
    project_video = models.FileField(upload_to='project_videos/', blank=True, null=True)  


class Project(models.Model):
    id  =  models.AutoField(primary_key = True)
    title = models.CharField(max_length = 250,blank=True,null= True)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='project_images/', blank=True, null=True)  

    def __str__(self):
        return self.title

class TechnicalSkill(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    icons = models.ImageField(upload_to = 'icons',null=True,blank=True)

    def __str__(self):
        return self.title

class InterpersonalSkill(models.Model):
    id = models.AutoField(primary_key = True)
    skill = models.CharField(max_length = 100)
    icon = models.ImageField(upload_to = 'icons',blank = True,null = True) 

    def __str__(self):
        return self.skill
    
class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')  # Répertoire de stockage des CV

    def __str__(self):
        return f"Resume {self.id}"

class Certification(models.Model):
    certificat = models.ImageField(upload_to='certifications/')  # Upload directory for certification images

    def __str__(self):
        return f"Certification {self.id}"