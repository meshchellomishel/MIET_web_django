from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=255)
  price = models.IntegerField()
  ship_date = models.DateTimeField()
  image = models.ImageField()
  discribtion = models.TextField()
  count = models.IntegerField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post', kwargs={'post_id': self.pk})


class Orders(models.Model):
  user = models.ForeignKey(User,
                           related_name='buyers',
                           on_delete=models.CASCADE)
  product = models.ForeignKey(Product,
                             related_name='card',
                             on_delete=models.CASCADE)
  ship_date = models.DateTimeField()
  count = models.IntegerField(default=0)

  
# class User(User):
#     image = models.ImageField(blank=True,
#                               null=True)
#     discribtion = models.TextField(blank=True,
#                                    null=True)
    
   