from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    price=models.PositiveIntegerField(blank=False,default=0)
    discriptions=models.TextField()
    created_at=models.TimeField(auto_now_add=True)
    created_date=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
