from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='images/')
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Webcontent(models.Model):
    Intro_text = RichTextField(blank=True, null=True)
    Free_trial_text = models.CharField(max_length=100)
    banner_video = models.FileField(upload_to='videos/')
    video_caption = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Intro_text
    
class BannerPost(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class RecommededPost(models.Model):
    title = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='images/')
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Call_to_Action1(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    link_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Call_to_Action2(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    link_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Call_to_Action3(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    link_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Services(models.Model):
    icon = models.ImageField(upload_to='images/')
    before_text = models.CharField(max_length=100)
    on_hover_text = models.CharField(max_length=100)

    def __str__(self):
        return self.before_text
    
class Report_Section(models.Model):
    intro_text = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    link_text = models.CharField(max_length=100)
    report_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class Final_Section(models.Model):
    section_name = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='images/')
    content = RichTextField(blank=True, null=True)
    link_text = models.CharField(max_length=100)

    def __str__(self):
        return self.section_name
