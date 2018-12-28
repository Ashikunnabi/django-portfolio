from django.contrib import admin

from .models import ResumeDetail, Experience, Education, ProgrammingLanguageIcons, Workflow, AwardCertification
from portfolio_app.models import Index

# Register your models here.
admin.site.register(ResumeDetail)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ProgrammingLanguageIcons)
admin.site.register(Workflow)
admin.site.register(AwardCertification)