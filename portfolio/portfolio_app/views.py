from django.core.paginator import Paginator
from django.shortcuts import render
import random

from .models import Application, Contact, Index, Message, Project, SocialLink


def index(request):
    person_detail = Index.objects.get(user_status="Active")             # Geting the active user info
    social_links  = SocialLink.objects.filter(user_id=person_detail.id)
    
    # Checking the file format
    bg_file_name  = str(person_detail.background_media)
    if bg_file_name.endswith(".mp4"):
        video = True
    else:
        video = False
        
    context = {
        'person_detail'                      : person_detail,
        'is_video'                           : video, 
        'social_links'                       : social_links,
    }
    return render(request, "portfolio_app/index.html", context)
    
    
def project_list(request):
    person_detail = Index.objects.get(user_status="Active")
    project_list  = Project.objects.filter(user_id=person_detail.id)
    # Pagination 
    paginator     = Paginator(project_list, 6) # Show 9 contacts per page
    page          = request.GET.get('page')
    projects      = paginator.get_page(page)
    
    context = {
        'person_detail'      : person_detail,
        'nav_active_home'    : 'active',
        'projects'           : projects,
    }
    return render(request, "portfolio_app/project_list.html", context)
    
    
def project_details(request, id):
    person_detail   = Index.objects.get(user_status="Active")
    projects        = Project.objects.filter(user_id=person_detail.id)
    project_details = Project.objects.get(user_id=person_detail.id, id=id)
    
    # Collecting list of ids except opened project and shuffle it to make random related projects
    project_ids = [project.id for project in projects if project_details.id != project.id]
    random.shuffle(project_ids)    
    try:
        related_project_1 = Project.objects.get(id=project_ids[0])  
    except:
        related_project_1 = None
    try:
        related_project_2 = Project.objects.get(id=project_ids[1])  
    except:
        related_project_2 = None
    try:
        related_project_3 = Project.objects.get(id=project_ids[2])  
    except:
        related_project_3 = None
    try:
        related_project_4 = Project.objects.get(id=project_ids[3])  
    except:
        related_project_4 = None
        
    if(related_project_1==None and related_project_2==None and related_project_3==None 
        and related_project_4==None):
        no_related_project = "No other project found."  
    else:
        no_related_project = None
        
    context = {
        'person_detail'             : person_detail,
        'nav_active_home'           : 'active',
        'projects'                  : projects,
        'project_details'           : project_details,
        'related_project_1'         : related_project_1,
        'related_project_2'         : related_project_2,
        'related_project_3'         : related_project_3,
        'related_project_4'         : related_project_4,
        'no_related_project'        : no_related_project,
    }
    return render(request, "portfolio_app/project_details.html", context)

        
def application(request):
    person_detail   = Index.objects.get(user_status="Active")
    applications    = Application.objects.filter(user_id=person_detail.id)
    
    context = {
        'person_detail'             : person_detail,
        'nav_active_applications'   : 'active',
        'applications'              : applications,
    }
    
    return render(request, "portfolio_app/application.html", context)

    
def message(request):
    person_detail   = Index.objects.get(user_status="Active")
    contact_page    = Contact.objects.get(user_id=person_detail.id)
    
    if request.method=="POST":
        name                 = request.POST.get('name')
        email                = request.POST.get('email')
        phone_number         = request.POST.get('phone')
        site_link            = request.POST.get('website')
        message              = request.POST.get('message')
    
        messaged = Message(
            user                 = person_detail,
            name                 = name,
            email                = email,
            phone_number         = phone_number,
            site_link            = site_link,
            message              = message
        )
        messaged.save()
    else:
        pass
        
    context = {
        'person_detail'             : person_detail,
        'nav_active_contact'        : 'active',
        'contact_page'              : contact_page,
    }
    return render(request, "portfolio_app/contact.html", context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    