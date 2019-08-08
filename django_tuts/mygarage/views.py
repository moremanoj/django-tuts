from django.shortcuts import render, redirect,  get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Post, BookService
from .forms import UserRegisterForm, ServiceBookingForm
from django.contrib import messages
from django.views.generic import DetailView


def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('garage-login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def Login(request):
    return render(request, 'login.html')

def History(request):
    if request.user.is_authenticated :
        if request.user.is_superuser :
            services = BookService.objects.filter(selected_date__lt=timezone.now)
        else:
            services = BookService.objects.filter(customer=request.user)
        context = {'services': services }
    return render(request, 'history.html', context)

# def DetailsPage(request) :
#     if request.method == 'POST':
#         form = ServiceBookingForm(request.POST)
#         form.status = 'Booked'
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.customer=request.user
#             obj.save()
#             messages.success(request, f'Successfully registered !')
#             return redirect('garage-history')
#     else:
#         form = ServiceBookingForm()
#     return render(request, 'service-detail.html', form)

class ServiceDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        service = get_object_or_404(BookService, pk=kwargs['pk'])
        context = {'service': service}
        if request.method == 'POST':
            service = ServiceBookingForm(request.POST)
            if service.is_valid():
                obj = service.save(commit=False)
                obj.customer=request.user
                obj.save()
                messages.success(request, f'Successfully registered !')
                return redirect('garage-history')
        else:
            form = ServiceBookingForm()
        return render(request, 'service-detail.html', context)        

def Service(request):
    if request.method == 'POST':
        form = ServiceBookingForm(request.POST)
        form.status = 'Booked'
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer=request.user
            obj.save()
            messages.success(request, f'Successfully registered !')
            return redirect('garage-history')
    else:
        form = ServiceBookingForm()
    return render(request, 'book-service.html', {'form': form} , None)

def AdminCalender(request):
    if request.user.is_authenticated :
        services = BookService.objects.filter(selected_date__gte=timezone.now)
        context = {'services': services }
    return render(request, 'admin-calender.html',context)