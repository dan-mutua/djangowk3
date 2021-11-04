from django.db import models
from datetime import datetime 
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save



class Subscriber(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Location(models.Model):
    location=models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.location


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    comment = models.TextField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    entry= models.ForeignKey('Entry', related_name="comments", on_delete=models.CASCADE, null=True,)


    objects = models.Manager()

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse('addcomment')

    @classmethod
    def show_projects(cls):
        comments = cls.objects.all()
        return comments
    def savecomment(self):
        self.save()

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('O', 'Other')
)


class UserProfile(models.Model):
    title= models.CharField(null=True, max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(null=True, max_length=255)
    phonenumber = models.IntegerField(null=True)
    bio = models.CharField(blank=True,max_length=255)
    userpic = CloudinaryField('image')
    gender = models.CharField(max_length=11, choices=GENDER_CHOICES, default='Male')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()


    @classmethod
    def getProfileByName(cls, username):
        uprofile = cls.objects.filter(username=username)
        return uprofile


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


