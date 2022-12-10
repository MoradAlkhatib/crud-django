from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



class Book(models.Model):
    
    name = models.CharField(max_length=200)
    page = models.IntegerField()
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(default='The Description Here...')
    image = models.CharField(max_length=255,default="No Image Provider")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
