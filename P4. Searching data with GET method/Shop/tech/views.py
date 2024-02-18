from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def Tiktok(request):
    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        email = data.get('email')
        Description = data.get('Description')
        bootha = request.FILES.get('bootha')

        tiktok.objects.create(
            name=name,
            email=email,
            Description=Description,
            bootha=bootha,

        )

        return redirect('/')

    queryset = tiktok.objects.all()


    if request.GET.get('search'):
        queryset = queryset.filter(Description__icontains = request.GET.get('search'))

    context = {'Tiktokers': queryset}

    return render(request, 'index.html', context)


def del_tiktoker(request, id):
    queryset = tiktok.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update_data(request, id):
    queryset = tiktok.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        email = data.get('email')
        Description = data.get('Description')
        bootha = request.FILES.get('bootha')

        queryset.name = name
        queryset.email = email
        queryset.Description = Description
        
        if bootha:
            queryset.bootha = bootha
        
        queryset.save()
        return redirect('/')

    context = {'insan': queryset}
    return render(request, 'update_data.html', context)