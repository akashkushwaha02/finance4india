from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/images',blank=True,null=True)

    def __str__(self):
        return self.title +' | '

    def get_absolute_url(self):
        #return reverse('details', args=(str(self.id)))
        return reverse('home')

