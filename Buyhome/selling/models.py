from django.db import models
from django.contrib.auth.models import User

class Properties(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)    
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/')
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('sold', 'Sold')], default='available')
    properties_geo = models.CharField(max_length=255)
    swimming_pool = models.BooleanField(default=False)
    emergency_exit = models.BooleanField(default=False)
    sold_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def is_sold(self):
        return self.status == 'sold'
