from django.core.files.storage import FileSystemStorage
from django.db import models




class users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.users


