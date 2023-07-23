from django.db import models

class Category(models.Model):
    hardwareType = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: {self.hardwareType}"


class Subcategory(models.Model):
    categoryName = models.CharField(max_length=50)
    Type = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.categoryName}"


class Item(models.Model):
    itemName = models.CharField(max_length=60)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='SerShip/static/images/')
    SubType = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.itemName} : {self.price}" 

    def display_image(self):
        return f'<img src="{self.image.url}" alt="{self.itemName}" width="100px" height="100px">'
