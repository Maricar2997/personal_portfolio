from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tools = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)

class Education(models.Model):
    university = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    year = models.CharField(max_length=100)

