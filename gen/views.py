from django.shortcuts import render, redirect
from .models import Generate
from .forms import Generateform
from django.contrib import messages
# Create your views here.


def Geneview(request):
    form = Generateform()
    if request.method == 'POST':
        form = Generateform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('suc')
        else:
            messages.info(request, form.errors) 
            return redirect('/')
    return render(request, 'contact.html')


def Success(request):
    # details = Generate.objects.filter(id=id)
    recentpost = Generate.objects.all().order_by('-id')[:1]
    # succ = Generate.objec
    content = {
        # 'succ': succ,
        'recentpost':recentpost,
        'succ':recentpost
    }
    return render(request, 'page.html', content)    


def Lastview(request):
    recent = Generate.objects.all().order_by('-id')[:1]

    content = {
        'recent':recent,
    }
    return render(request, 'page2.html', content)    