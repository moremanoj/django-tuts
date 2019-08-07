from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class BookService(models.Model):
    service_type = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    vehicle_type =  models.CharField(max_length=100)
    vehicle_make =  models.CharField(max_length=100)
    vehicle_licence = models.CharField(max_length=100)
    vehicle_engine_type =  models.CharField(max_length=100)
    customer_comments = models.TextField()
    selected_date = models.DateTimeField( default=timezone.now)
    status = models.CharField(max_length=100, default='Booked')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.service_type