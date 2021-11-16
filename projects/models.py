from django.contrib.auth import get_user_model
from django.db import models

experience_choices = [('not_set', 'not_set'), ('0-3', '0-3'), ('3-5','3-5'), ('5-7','7-10'), ('10+','10+')]

gender_choices = [('not_set', 'not_set'), ('Female', 'Female'), ('Non-binary','Non-binary'),]

class Profile(models.Model):
    bio = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    photo = models.URLField()
    gender = models.CharField(
        max_length=50,
        choices=gender_choices,
        default='not_set'
        ) 
    experience = models.CharField(
        max_length=100,
        choices=experience_choices,
        default='not_set',
    )
    role = models.CharField(max_length=250)
    company = models.CharField(max_length=250) 
    facts = models.CharField(max_length=150)
    linkedin = models.URLField()
    status = models.CharField(max_length=250)
    date_created = models.DateTimeField()
