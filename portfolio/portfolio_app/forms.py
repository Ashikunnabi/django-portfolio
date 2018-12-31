from django import forms

from .models import Message

           
class MessageForm(formss.ModelForms):
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
    
    
    
    
    
    
    