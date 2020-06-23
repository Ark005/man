from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=300, blank=True)
    bio = models.TextField(blank=True,max_length=1)
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return self.title
 


