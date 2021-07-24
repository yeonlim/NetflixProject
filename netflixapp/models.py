from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Netflix(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    genre_Choices = (
        ('로맨스','로맨스'),
        ('호러/스릴러','호러/스릴러'),
        ('SF/판타지','SF/판타지'),
        ('버라이어티/예능','버라이어티/예능'),
        ('애니메이션','애니메이션'),
        ('다큐멘터리','다큐멘터리'),
        )
    genre = models.TextField(choices=genre_Choices)
    score = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    img = models.ImageField(upload_to="netflix/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source = 'img', processors=[ResizeToFill(120,100)])

    def __str__(self):
          return self.title

    def summary(self):
        return self.content[:50]