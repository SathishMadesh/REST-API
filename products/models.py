from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField()
    imgurl = models.URLField()
    price = models.FloatField()
    quantity = models.IntegerField()


    def __str__(self):
        return self.name