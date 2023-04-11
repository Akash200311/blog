from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField



# Create your models here.
class short_descriptions(models.Model):
    Title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/')
    choose=models.ForeignKey("types",related_name="choice", on_delete=models.CASCADE)
    Desc=models.TextField()
    new_slug1=AutoSlugField(populate_from='Title',unique=True,null=True,default=None)  
    share_key1=models.IntegerField(default=None,unique=True)
    def __str__(self):
        return self.Title
    
    

class types(models.Model):
    types=models.CharField(max_length=50)
    def __str__(self):
        return self.types
    

class template(models.Model):
    Title=models.CharField(max_length=50)
    choice=models.ForeignKey("types", related_name="type", on_delete=models.CASCADE)
    heading=models.CharField(max_length=50)
    intro_description=RichTextField()
    intro_description=RichTextField()
    time=models.CharField( max_length=50)
    image_1=models.ImageField(upload_to='media')
    image_2=models.ImageField(upload_to='media')
    image_3=models.ImageField(upload_to='media')
    image_4=models.ImageField(upload_to='media')

   
   
    description=RichTextField()
    question1=models.TextField(default="")
    answer1=models.TextField(default="")   
    question2=models.TextField(default="")
    answer2=models.TextField(default="")   
    question3=models.TextField(default="")
    answer3=models.TextField(default="") 
    new_slug2=AutoSlugField(populate_from='Title',unique=True,null=True,default=None)  
    share_key2=models.IntegerField(default=None,unique=True)
    def __str__(self):
        return self.Title
class profile(models.Model):
    profile_pic=models.ImageField(upload_to='media')
    fb_link=models.CharField(max_length=100,default=None)
    insta_link=models.CharField(max_length=100,default=None)
    twitter_link=models.CharField(max_length=100,default=None)





