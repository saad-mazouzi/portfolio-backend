from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'aboutme', AboutMeViewSet)
router.register(r'experiences',ProfessionalExperienceViewSet)
router.register(r'techskills',TechnicalSkillViewSet)
router.register(r'interperso',InterpersonalSkillViewset)
router.register(r'contacts',ContactViewset)
router.register(r'resume',ResumeViewset)
router.register(r'projects',ProjectViewset)
router.register(r'certifications',CertificationViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]

