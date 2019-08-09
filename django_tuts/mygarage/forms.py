from django import forms
from .models import BookService
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .utils import getDisableDates
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


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
    disable_dates = []
    mindate = "{}".format(timezone.now().date())
    selected_date = forms.DateTimeField( widget=DateTimePicker(
        options={
            'minDate': mindate,
            'maxDate': '2029-01-20',
            'format': 'L',
			'disabledDates' : disable_dates,
            'daysOfWeekDisabled': [0]
        },
        attrs={
            'min' : timezone.now().date()
        }
    ),)
    service_type = forms.CharField(widget=forms.Select(choices=SERVICE_TYPES))
    vehicle_type = forms.CharField(widget=forms.Select(choices=VEHICLE_TYPE))
    vehicle_make = forms.CharField(widget=forms.Select(choices=VEHICLE_MAKE))
    
    class Meta:
        model = BookService
        widgets =  {
            'selected_date': forms.DateInput(attrs={'min': timezone.now().date(), 'type':'date','id':'datepicker01', 'class':'form-control md-form datepicker'}),
        }
        fields = ['service_type', 'customer_name', 'contact_details', 
                  'vehicle_type', 'vehicle_make','vehicle_licence', 'vehicle_engine_type',
                  'customer_comments','selected_date']