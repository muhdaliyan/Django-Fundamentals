from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def Tiktok(request):
    if request.method=="POST":
        data = request.POST

        name = data.get('name')
        email = data.get('email')
        Description = data.get('Description')
        bootha = request.FILES.get('bootha')

        tiktok.objects.create(
            name = name,
            email = email,
            Description = Description,
            bootha = bootha,
            
        )

        return redirect('/')
    
    queryset = tiktok.objects.all()
    context = {'Tiktokers': queryset}

    return render(request, 'index.html', context)