from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from bloodbank.models import BloodBank
from django.db.models import Sum 
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def dash(request):
    bloodbanks = BloodBank.objects.all()
    context={}
    context['bloodbanks'] = bloodbanks
    total_quantity = bloodbanks.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    context['total_quantity'] = total_quantity
    return render(request,'registration/dash.html',context)

from .forms import DonorForm
def donor_form_view(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form = DonorForm()
    
    return render(request, 'donor_form.html', {'form': form})

