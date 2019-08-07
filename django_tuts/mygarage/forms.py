from django import forms
from .models import BookService
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget

SERVICE_TYPES = [ ('orange', 'Oranges'), ('mango', 'manogoes'), ('banana', 'bananas')]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ServiceBookingForm(forms.ModelForm):
    selected_date = forms.DateField(widget=AdminDateWidget)    
    service_type = forms.CharField(widget=forms.Select(choices=SERVICE_TYPES)) 
    
    class Meta:
        model = BookService
        widgets =  {
            'selected_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ['service_type', 'customer_name', 'contact_details', 
                  'vehicle_type', 'vehicle_make','vehicle_licence', 'vehicle_engine_type',
                  'customer_comments','selected_date']