from django.db import models
from django.conf import settings
# Create your models here.

class Course(models.Model):
    course_id = models.CharField(primary_key = True)
    course_name = models.CharField()
    
#user groups usage signals usage