from django.db import models

# Create your models here.

class Booking(models.Model):

    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(default=6)
    booking_date = models.DateField()

class Menu(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=1, decimal_places=1)
    inventory = models.IntegerField(default=1)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
