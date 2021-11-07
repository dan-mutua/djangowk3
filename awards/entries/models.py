from django.db import models
from datetime import datetime 
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save






class Comment(models.Model):
    entry= models.ForeignKey('Entry', related_name="comments", on_delete=models.CASCADE, null=True,)
    name = models.CharField(max_length=200,null=True)
    body= models.TextField(null=True)
    date_added=models.DateTimeField(auto_now_add=True,null=True)



    ()


    def __str__(self):
        return '%s-%s' % (self.entry.title,self.name)
  






class Entry(models.Model):
    title = models.CharField(null=True, max_length=255)
    name = models.CharField(null=True, max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    userpic = CloudinaryField('image', null=True)
    description = models.CharField(blank=True,max_length=255)
    livelink = models.URLField(blank=True, null=True)
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(User, related_name="projectlikes")
    likecount = models.BigIntegerField(default='0')

 

    def totallikes(self):
        return self.likes.count()
    # objects = models.Manager()

    def get_absolute_url(self):
        return reverse('findpost', kwargs={'pk': self.pk})

    @classmethod
    def show_projects(cls):
        entriess = cls.objects.all()
        return entriess


    @classmethod
    def getprojectbyid(cls, id):
        entriess = cls.objects.filter(id=id)
        return entriess

    @classmethod
    def getprojectbytitle(cls, searchtitle):
        getentry= cls.objects.filter(title=searchtitle)
        return getentry

class ProjectRating(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField()


