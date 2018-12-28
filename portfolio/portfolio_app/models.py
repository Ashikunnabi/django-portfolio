from django.db import models


class Index(models.Model):
    title                           = models.CharField(max_length=50)
    name                            = models.CharField(max_length=20)
    description                     = models.TextField(max_length=150)
    button                          = models.CharField(max_length=20)
    overlay_and_button_color        = models.CharField(max_length=30, default="#cd9557")
    button_hover                    = models.CharField(max_length=30, default="#ba7c37")
    background_and_icon_color       = models.CharField(max_length=30, default="rgba(0,46,102,.8)")
    background_and_icon_hover_color = models.CharField(max_length=30, default="#002e66")
    background_media                = models.FileField(default="bg.mp4", null=True)
    media_position_top              = models.CharField(max_length=10, default="50%")
    media_position_left             = models.CharField(max_length=10, default="50%")
    footer                          = models.CharField(max_length=10, default="Copyright &copy; ashikunnabi.pythonanywhere.com | 2018")
    user_status                     = models.CharField(max_length=8, default="Inactive")
    
    
    class Meta:
        verbose_name = "Index page"
    
    def __str__(self):
        return self.name    
    

class SocialLink(models.Model): 
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=300)
    icon = models.CharField(max_length=140)
    user = models.ForeignKey('Index', on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.name +" - "+ self.user.name)
        
        
class Project(models.Model):
    user                 = models.ForeignKey('Index', on_delete=models.CASCADE)
    name                 = models.CharField(max_length=100)
    sub_name             = models.CharField(max_length=100, blank=True)
    description          = models.TextField(max_length=400)
    requirments          = models.TextField(max_length=400)
    site_name            = models.CharField(max_length=100)
    site_link            = models.CharField(max_length=500)
    site_link_icon       = models.CharField(max_length=500, default='<i class="fas fa-eye"></i>')
    media                = models.FileField(default="Capture.PNG", null=True)
    
    def __str__(self):
        return (self.name +" - "+ self.user.name)     

        
class Application(models.Model):
    user          = models.ForeignKey('Index', on_delete=models.CASCADE)
    name          = models.CharField(max_length=20)
    icon          = models.CharField(max_length=60)
    icon_color       = models.CharField(max_length=30, default="rgba(0,46,102,.8)")
    icon_hover_color = models.CharField(max_length=30, default="#002e66")
    file          = models.FileField()
    
    def __str__(self):
        return (self.name +" - "+ self.user.name)  
        

        
class Contact(models.Model):
    user                  = models.ForeignKey('Index', on_delete=models.CASCADE)
    title                 = models.CharField(max_length=100)
    sub_title             = models.CharField(max_length=100)
    button_text           = models.CharField(max_length=100, blank=True)
    button_color          = models.CharField(max_length=500, blank=True)
    
    
    
    class Meta:
        verbose_name = "Contact page"
        
    def __str__(self):
        return (self.title +" - "+ self.user.name)
    
           
class Message(models.Model):
    user                 = models.ForeignKey('Index', on_delete=models.CASCADE)
    name                 = models.TextField(max_length=400)
    email                = models.TextField(max_length=400)
    phone_number         = models.CharField(max_length=100, blank=True)
    site_link            = models.CharField(max_length=500, blank=True)
    message              = models.TextField()
    date                 = models.DateField(auto_now=True)
    
    
    
    class Meta:
        verbose_name = "Others message"
        
    def __str__(self):
        return (self.name +" - "+ self.user.name)
    
    
    
    
    
    
    