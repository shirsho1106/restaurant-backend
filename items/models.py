from django.db import models
# Create your models here.

class Item(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.TextField(default="burger")
    title = models.TextField(default="food")
    description = models.TextField(default="delicious food")
    image = models.ImageField(upload_to='media', default='default.jpg')
    price = models.TextField(default="money")