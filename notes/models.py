from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,null=True)
    branch = models.CharField(max_length=30)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=10  )
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=10)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30)
    description = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=15)

    #def __str__(self):
        #return self.user.username