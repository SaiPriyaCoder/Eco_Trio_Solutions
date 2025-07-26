from django.db import models


class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    occupation = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    signup_time = models.DateTimeField()
    device_info = models.TextField()

    def __str__(self):
        return self.first_name

from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')  # uploaded to MEDIA_ROOT/team/

    def __str__(self):
        return self.name


class Collaboration(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='collaborations/')  # Store images in MEDIA_ROOT/collaborations
    website_link = models.URLField(blank=True, null=True)
    #github_link = models.URLField(blank=True)
    # linkedin_link = models.URLField(blank=True)
    # twitter_link = models.URLField(blank=True)
    # instagram_link = models.URLField(blank=True)
    # facebook_link = models.URLField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='job_icons/')  # optional field
    description = models.TextField()

    def __str__(self):
        return self.title