from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    gerne=models.CharField(max_length=200)
    isbn=models.CharField(max_length=200)
    published_date=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to="images,",null=True)
      
      
      
