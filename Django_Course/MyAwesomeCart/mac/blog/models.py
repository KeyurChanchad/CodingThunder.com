from django.db import models

# Create your models here.
class BlogPost(models.Model):
    blogpost_id  = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    heading1 = models.CharField(max_length=300)
    content1 = models.CharField(max_length=5000)
    heading2 = models.CharField(max_length=300)
    content2 = models.CharField(max_length=5000)
    heading3 = models.CharField(max_length=300)
    content3 = models.CharField(max_length=5000)
    pub_date = models.DateField(default="")
    thumbnail = models.ImageField(upload_to='blog/images', default = "")

    def __str__(self):
        return self.title