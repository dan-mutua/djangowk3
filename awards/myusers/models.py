from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from PIL import Image
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=200)
    contact = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save_profile(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile
        
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    
class tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def save_tags(self):
        self.save()
        
    def delete(self):
        self.delete()