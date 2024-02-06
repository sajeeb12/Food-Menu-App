from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE, default = 1)
    item_name = models.CharField(max_length = 250)
    item_desc = models.CharField(max_length=250)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default = "https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_500,h_376,al_c,lg_1,q_80,enc_auto/food-placeholder.jpg")

    def __str__(self):
        return self.item_name
    