from django.db import models
from portfolio_app.models import Index

class Experience(models.Model):
    user          = models.ForeignKey(Index, on_delete=models.CASCADE)
    designation   = models.CharField(max_length=100, null=True, blank=True)
    company       = models.CharField(max_length=100, null=True, blank=True)
    time          = models.CharField(max_length=100, null=True, blank=True)
    description   = models.TextField(max_length=500, null=True, blank=True)	

    def __str__(self):
        return (self.designation +" - "+ self.user.name)

class Education(models.Model):
    user          = models.ForeignKey(Index, on_delete=models.CASCADE)
    institution   = models.CharField(max_length=100)
    degree        = models.CharField(max_length=100)
    track         = models.CharField(max_length=100)
    gpa           = models.CharField(max_length=5)
    time          = models.CharField(max_length=100)
	
    def __str__(self):
        return (self.degree +" - "+ self.user.name)

class AwardCertification(models.Model):
    user           = models.ForeignKey(Index, on_delete=models.CASCADE)
    title          = models.CharField(max_length=100)
    company        = models.CharField(max_length=100)
    time           = models.CharField(max_length=100)
	
    def __str__(self):
        return (self.title +" - "+ self.user.name)	
	

class ResumeDetail(models.Model):
    user            = models.ForeignKey(Index, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    picture         = models.FileField(default="Capture.PNG", null=True)
    address         = models.CharField(max_length=100)
    mobile          = models.CharField(max_length=14)
    email           = models.EmailField(max_length=254)
    about           = models.TextField(max_length=300)
    facebook_link   = models.CharField(max_length=200, null=True, blank=True)
    twitter_link    = models.CharField(max_length=200, null=True, blank=True)
    linkedin_link   = models.CharField(max_length=200, null=True, blank=True)
    github_link     = models.CharField(max_length=200, null=True, blank=True)
    interests       = models.TextField(max_length=500)

    def __str__(self):
        return (self.first_name +" - "+ self.user.name)
		
		
class ProgrammingLanguageIcons(models.Model):
    user      = models.ForeignKey(Index, on_delete=models.CASCADE)
    name      = models.CharField(max_length=30)
    icon      = models.CharField(max_length=60)

    def __str__(self):
        return (self.name +" - "+ self.user.name)
    		
class Workflow(models.Model):
    user      = models.ForeignKey(Index, on_delete=models.CASCADE)
    name      = models.CharField(max_length=100)

    def __str__(self):
        return (self.name +" - "+ self.user.name)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    