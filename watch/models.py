from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid
from django.db.models.signals import post_save
# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.png', upload_to='profile_pics')
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path) 

class Neighborhood(models.Model):
    neighborhood_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    picture=models.ImageField(upload_to=user_directory_path, verbose_name='Picture', null=False)
    location=models.TextField(max_length=300, verbose_name='Location')
    occupants_count= models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def search_by_name(cls,search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods


    def __str__(self):
        return self.name

class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture=models.ImageField(upload_to=user_directory_path, verbose_name='Picture', null=False)
    caption=models.TextField(max_length=300, verbose_name='Caption')
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     id = models.AutoField(primary_key=True)
#     neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
#     email_address = models.CharField(max_length=100)
 
#     def __str__(self):
#         return self.name

class Business(models.Model):    
    name = models.CharField(max_length=100)
    picture=models.ImageField(upload_to=user_directory_path, verbose_name='Picture', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=100)

    @classmethod
    def search_by_name(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

 
    def __str__(self):
        return self.name

class HealthCentre(models.Model):
    name = models.CharField(max_length=100)
    picture=models.ImageField(upload_to=user_directory_path, verbose_name='Picture', null=False)
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True,blank=True)

 
    def __str__(self):
        return self.name

class PoliceAuthority(models.Model):
    name = models.CharField(max_length=100)
    picture=models.ImageField(upload_to=user_directory_path, verbose_name='Picture', null=False)  
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True,blank=True)
 
    def __str__(self):
        return self.name