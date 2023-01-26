from django.db import models

# Create your models here.
class Student(models.Model):
    sId = models.CharField(max_length=10)
    sName = models.CharField(max_length=30)
    sPassword = models.CharField(max_length=30)
    sEmail = models.EmailField()

class Blog(models.Model):
    user_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    postDetail = models.CharField(max_length=200)
    publisherName = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/')


