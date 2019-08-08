from django.shortcuts import render, redirect,  get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Post, BookService
from .forms import UserRegisterForm, ServiceBookingForm
from django.contrib import messages
from django.views.generic import View, DetailView
from .utils import render_to_pdf
from django.template.loader import get_template

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
            # messages.success(request, f'Account created for {username}!')
            return redirect('garage-login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def Login(request):
    return render(request, 'login.html')

def History(request):
    if request.user.is_authenticated :
        if request.user.is_superuser :
            services = BookService.objects.all()
        else:
            services = BookService.objects.filter(customer=request.user)
        context = {'services': services }
    return render(request, 'history.html', context)

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class ServiceDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        service = get_object_or_404(BookService, pk=kwargs['pk'])
        context = {'service': service}
        return render(request, 'service-detail.html', context)        

class JobDetailView(DetailView):
        def get(self, request, *args, **kwargs):
            service = get_object_or_404(BookService, pk=kwargs['pk'])
            form = ServiceBookingForm()
            context = {'service': service, 'form': form}
            if request.method == 'POST':
                if 'print' in request.POST:
                    pdf = GeneratePDF(request.POST)
                if 'update' in request.POST:
                    form = ServiceBookingForm(request.POST)
                    if form.is_valid():
                        obj = service.save(commit=False)
                        obj.save()
                    # messages.success(request, f'Successfully registered !')
                    return redirect('garage-jobs')
            return render(request, 'job-detail.html', context)
    
def Service(request):
    if request.method == 'POST':
        form = ServiceBookingForm(request.POST)
        form.status = 'Booked'
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer=request.user
            obj.save()
            # messages.success(request, f'Successfully registered !')
            return redirect('garage-history')
    else:
        form = ServiceBookingForm()
    return render(request, 'book-service.html', {'form': form} , None)

def Jobs(request):
    if request.user.is_authenticated :
        services = BookService.objects.all()
        context = {'services': services }
    return render(request, 'jobs.html',context)