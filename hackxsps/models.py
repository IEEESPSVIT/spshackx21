from django.db import models

# Create your models here.
class Registration(models.Model):
    
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    
    phone = models.CharField(max_length=10)
    
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=1)
    stream = models.CharField(max_length=60)
    track = models.CharField(max_length=60)
    teamnum = models.CharField(max_length=1)
    teamname = models.CharField(max_length=50)
    teammemname1 = models.CharField(max_length=100)
    teammememail1 = models.EmailField(max_length=100)
    teammemname2 = models.CharField(max_length=100)
    teammememail2 = models.EmailField(max_length=100)
    teammemname3 = models.CharField(max_length=100)
    teammememail3 = models.EmailField(max_length=100)
    teammemname4 = models.CharField(max_length=100)
    teammememail4 = models.EmailField(max_length=100)




    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.teamnum