from django.db import models

# Create your models here.
class Category(models.Model): # табл с категориями
    name = models.CharField(max_length=30)


class Post(models.Model): # табл с постами
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #вр-мя/дата доб-я записи
    last_modified = models.DateTimeField(auto_now=True) # вр-мя/дата редак-я записи
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=40)
    body= models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)

