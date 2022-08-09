from django.shortcuts import render, redirect
from .models import Generate,PaymentSlip
from .forms import Generateform, Slip
from django.contrib import messages
# Create your views here.


def HomeView(request):

    return render(request,  'index.html')

def Geneview(request):
    form = Generateform()
    if request.method == 'POST':
        form = Generateform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('suc')
        else:
            messages.info(request, form.errors) 
            return redirect('generate')
    return render(request, 'contact.html', {'form': form})


def Success(request):
    # details = Generate.objects.filter(id=id)
    recentpost = Generate.objects.all().order_by('-id')[:1]
    # succ = Generate.objec
    # list_for_random = range(1000000)
    content = {
        
        # 'recentpost':recentpost,
        'recentpost':recentpost
    }
    return render(request, 'page.html', content)    


def Lastview(request):
    recent = Generate.objects.all().order_by('-id')[:1]

    content = {
        'recent':recent,
    }
    return render(request, 'page2.html', content)    


def paymentview(request):
    form = Slip()
    if request.method == 'POST':
        form = Slip(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('sum')
        else:
            messages.info(request, form.errors) 
            return redirect('payment')
    return render(request, 'payment.html')    

def pay(request):
    recenting = PaymentSlip.objects.all().order_by('-id')[:1]
    list_for_random = range(2000000000)
    
    content = {
        'recenting':recenting,
        'list_for_random': list_for_random,
    }
    return render(request, 'payment_1.html', content)      