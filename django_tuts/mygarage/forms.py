from django import forms
from .models import BookService
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget

SERVICE_TYPES = [ ('Annual Service', 'Annual Service'), ('Major Service', 'Major Service'),
                  ('Repairs/Faults', 'Repairs/Faults'), ('Major Repairs', 'Major Repairs')]
VEHICLE_TYPE = [('Hatchback','Hatchback'), ('Sedan','Sedan'), ('MPV','MPV'),
                ('SUV','SUV'), ('Crossover','Crossover'),('Coupe','Coupe')]
VEHICLE_MAKE = [('Maruti Suzuki Alto','Maruti Suzuki Alto'), ('Maruti Suzuki Alto K10','Maruti Suzuki Alto K10'),	
                ('Renault Kwid','Renault Kwid'), ('Hundai Santro','Hundai Santro'),('Maruti Suzuki Swift','Maruti Suzuki Swift'),
                ('Tata Tiago','Tata Tiago'),('Maruti Suzuki Celerio','Maruti Suzuki Celerio'),
                ('Ford Figo','Ford Figo'), ('Maruti Suzuki baleno','Maruti Suzuki baleno'),	('Hundai Elite i20','Hundai Elite i20')]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
                
class ServiceBookingForm(forms.ModelForm):
    selected_date = forms.DateTimeField(widget=forms.TextInput(attrs={'minDate': timezone.now, 'type':'date','id':'datepicker'}))
    service_type = forms.CharField(widget=forms.Select(choices=SERVICE_TYPES))
    vehicle_type = forms.CharField(widget=forms.Select(choices=VEHICLE_TYPE))
    vehicle_make = forms.CharField(widget=forms.Select(choices=VEHICLE_MAKE))
    class Meta:
        model = BookService
        widgets =  {
            'selected_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ['service_type', 'customer_name', 'contact_details', 
                  'vehicle_type', 'vehicle_make','vehicle_licence', 'vehicle_engine_type',
                  'customer_comments','selected_date']