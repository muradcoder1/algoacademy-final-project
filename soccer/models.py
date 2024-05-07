from django.db import models

# Create your models here.
class team(models.Model):
      oynanan_oyun=models.IntegerField(max_length=50)
      qalibiyet=models.IntegerField(max_length=50)
      meglubiyet=models.IntegerField(max_length=50)
      total=models.IntegerField(max_length=50)
class blog(models.Model):
      news_name=models.CharField(max_length=50)
      about_the_news=models.TextField(max_length=500)
      release_date = models.DateField(max_length=50)
      
      def __str__(self):
            return self.title