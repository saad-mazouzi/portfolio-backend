from django.contrib import admin
from .models import AboutMe,Contact,Project,TechnicalSkill,InterpersonalSkill,ProfessionalExperience,Resume,Certification
# Register your models here.

admin.site.register(AboutMe)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(TechnicalSkill)
admin.site.register(InterpersonalSkill)
admin.site.register(ProfessionalExperience)
admin.site.register(Resume)
admin.site.register(Certification)