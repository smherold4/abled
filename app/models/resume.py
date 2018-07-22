from django.db import models
from .candidate import Candidate

class Resume(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250)
    filetype = models.CharField(max_length=250)
    filesize = models.IntegerField()
    fileurl = models.CharField(max_length=450)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    candidate = models.ForeignKey(Candidate, default="general", on_delete=models.CASCADE) # a foreignkey