from django.db import models

# Create your models here.
class User_details(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    profile_pic=models.ImageField(upload_to='profile_pics/',null=True,blank=True)

    def __str__(self):
        return self.name