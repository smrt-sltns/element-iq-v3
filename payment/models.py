from django.db import models

class TokenOffer(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    price_id = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)  # might not be necessary

    def __str__(self):
        return f"${self.price} - {self.name}"