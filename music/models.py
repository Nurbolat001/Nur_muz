from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name




class Music(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio/')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.title



class NewsAppUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username