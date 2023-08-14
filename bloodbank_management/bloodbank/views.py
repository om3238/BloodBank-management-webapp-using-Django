from django.shortcuts import render, get_object_or_404, redirect
from .models import BloodBank
from .forms import BloodBankForm
from django.db.models import Q

def bloodbank_list(request):
    # Handling filter parameters from the URL query string
    query = request.GET.get('q')
    blood_group = request.GET.get('blood_group')
    location = request.GET.get('location')
    quantity = request.GET.get('quantity')

    # Initial queryset to show all blood bank entries
    queryset = BloodBank.objects.all()

    # Apply filtering based on user input (if any)
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(blood_group__icontains=query) |
            Q(quantity__icontains=query)
        )
    if blood_group:
        queryset = queryset.filter(blood_group__iexact=blood_group)
    if location:
        queryset = queryset.filter(location__icontains=location)

    context = {
        'bloodbanks': queryset
    }
    return render(request, 'bloodbank/bloodbank_list.html', context)


def bloodbank_add(request):
    if request.method == 'POST':
        form = BloodBankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloodbank_list')
    else:
        form = BloodBankForm()
    return render(request, 'bloodbank/bloodbank_form.html', {'form': form})

def bloodbank_update(request, pk):
    bloodbank = get_object_or_404(BloodBank, pk=pk)
    if request.method == 'POST':
        form = BloodBankForm(request.POST, instance=bloodbank)
        if form.is_valid():
            form.save()
            return redirect('bloodbank_list')
    else:
        form = BloodBankForm(instance=bloodbank)
    return render(request, 'bloodbank/bloodbank_form.html', {'form': form})


def bloodbank_delete(request, pk):
    bloodbank = get_object_or_404(BloodBank, pk=pk)
    if request.method == 'POST':
        bloodbank.delete()
        return redirect('bloodbank_list')
    
    return render(request, 'bloodbank/bloodbank_delete.html', {'bloodbank': bloodbank})


