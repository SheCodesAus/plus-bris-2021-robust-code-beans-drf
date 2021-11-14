from django.db import models

class Profile(models.Model):
    bio = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    photo = models.URLField()
    gender = models.CharField(max_length=250) 
    # experience = models.IntegerField(3)
    role = models.CharField(max_length=250)
    company = models.CharField(max_length=250) 
    facts = models.CharField(max_length=150)
    # date_created = models.DateField()
    linkedin = models.URLField()
    status = models.CharField(max_length=250)
