from django.utils import timezone
from django.db import models

class Rating(models.Model):
    numReviews = models.IntegerField()
    avgRating = models.FloatField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

class BlogPost(models.Model):
    posttitle = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    publicationDate = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique =True, max_length =255, null = True, blank=True)
    status = models.CharField(max_length=1, default=0)
    def is_pre_covid(self):
        #check if publication_date is pre covid means before 20 Mar 2020
        return self.publicationDate < timezone.datetime(2020, 3, 20 , tzinfo=timezone.utc)
