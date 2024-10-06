from rest_framework import serializers
from .models import Contact,AboutMe,TechnicalSkill,InterpersonalSkill,ProfessionalExperience,Project,Resume,Certification

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutMe
        fields='__all__'

# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Education
#         fields='__all__'

class TechnicalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=TechnicalSkill
        fields='__all__'

class InterpersonalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=InterpersonalSkill
        fields='__all__'

class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExperience
        fields = '__all__' 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resume
        fields='__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields='__all__'