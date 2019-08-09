from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Post, BookService
from .forms import UserRegisterForm, ServiceBookingForm
from django.contrib import messages
from django.views.generic import View, DetailView, ListView, UpdateView
from .utils import render_to_pdf, getServiceData 
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        context = getServiceData(kwargs['pk'])
        template = get_template('pdf/invoice.html')
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


class JobUpdateView(UpdateView):
    def get(self, request, *args, **kwargs):
        model = BookService
        form = ServiceBookingForm()
        context = { 'service': get_object_or_404(BookService, pk=kwargs['pk'])}
        return render(request, 'job-detail.html', context)
        

class JobListView(ListView):
    model = BookService
    template_name = 'jobs.html'
    context_object_name = 'services'
    

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
            services = BookService.objects.filter(customer=request.user)
            context = {'services': services }
        return render(request, 'history.html', context)
    