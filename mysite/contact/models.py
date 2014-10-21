from django.db import models

class email_list(models.Model):
    ID = models.IntegerField(max_length=5)
    email = models.CharField(max_length=30)
    content = models.CharField(max_length=200)

    
    def __unicode__(self):
        return self.email
        
    class meta:
        ordering = ['ID']
    

