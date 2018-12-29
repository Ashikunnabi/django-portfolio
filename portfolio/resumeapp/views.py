from django.shortcuts import render

from .models import ResumeDetail, Experience, Education, ProgrammingLanguageIcons, Workflow, AwardCertification
from portfolio_app.models import Index

# Create your views here.
def index(request):
    person_detail             = Index.objects.get(user_status="Active")
    resume                    = ResumeDetail.objects.get(user_id=person_detail.id)
    experience                = Experience.objects.filter(user_id=person_detail.id)
    education                 = Education.objects.filter(user_id=person_detail.id)
    programming_languages     = ProgrammingLanguageIcons.objects.filter(user_id=person_detail.id)
    workflows                 = Workflow.objects.filter(user_id=person_detail.id)
    awardCertification        = AwardCertification.objects.filter(user_id=person_detail.id)
	
    context = {
        'resume'               : resume, 
        'nav_active_about'     : 'active',
        'experience'           : experience, 
        'education'            : education, 
        'programming_languages': programming_languages, 
        'workflows'            : workflows, 
        'awardCertification'   : awardCertification, 
        'name'                 : person_detail.name,
        'person_detail'        : person_detail,
    }
    return render(request, 'resumeapp/about.html', context)
