from django.db import models

class Profile(models.Model):
    bio = models.CharField(max_length=250)
    first_name = models.TextField()
    photo = models.URLField()
    gender = models.TextField() 
    experience = models.IntegerField()
    role = models.TextField()
    company = models.TextField() 
    facts = models.CharField(max_length=150)
    date_created = models.DateField()
    linkedin = models.URLField()
    status = models.TextField()
