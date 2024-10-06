from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import AboutMeSerializer,ContactSerializer,ProfessionalExperienceSerializer,TechnicalSkillSerializer,InterpersonalSkillSerializer,ProjectSerializer,ResumeSerializer,CertificationSerializer
from .models import AboutMe,Contact,TechnicalSkill,InterpersonalSkill,Project,ProfessionalExperience,Resume,Certification
from .sendinblue_service import send_contact_email


class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class ProfessionalExperienceViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalExperience.objects.all()
    serializer_class = ProfessionalExperienceSerializer

class TechnicalSkillViewSet(viewsets.ModelViewSet):
    queryset = TechnicalSkill.objects.all()
    serializer_class = TechnicalSkillSerializer

class InterpersonalSkillViewset(viewsets.ModelViewSet):
    queryset=InterpersonalSkill.objects.all()
    serializer_class=InterpersonalSkillSerializer

from .sendinblue_service import send_contact_email

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()  # Sauvegarde l'objet Contact
        send_contact_email(contact)  # Envoie l'email avec le message

class ResumeViewset(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CertificationViewset(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer