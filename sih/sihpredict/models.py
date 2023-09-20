
from django.db import models


# Create your models here.


class news(models.Model):
    heading=models.TextField()
    content=models.TextField()
    urls=models.TextField()
    source=models.TextField()

class newssource(models.Model):
    NewsSource=models.TextField()