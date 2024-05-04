from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactForm

# Create your views here.
def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    return render(request, "index.html",{'flans': public_flans})

def about(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, "about.html",{'flans':private_flans})

def welcome(request):
    return render(request, "welcome.html",{})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('contact_exitoso')
    else:
        form = ContactForm()
    return render(request, "contact.html",{'form':form})

def contact_exitoso(request):
    return render(request, 'contact_exitoso.html', {})