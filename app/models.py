from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 255,default="")
    slug = models.SlugField(default="")
    intro = models.TextField(default="")
    body = models.TextField(default="")
    posted_date = models.DateTimeField(auto_now_add = True)

