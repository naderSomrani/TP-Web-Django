from django.db import models

# Create your models here.


class Customer(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    address = models.CharField(max_length=80)
    email = models.CharField(max_length=40, default="mail@mail.com")
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    order_total = models.FloatField()

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Other')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
