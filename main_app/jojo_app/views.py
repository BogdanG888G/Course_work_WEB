# jojo_app/views.py

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from main_app.models import Stand
from .forms import StandForm

def home(request):
    return render(request, 'home.html')

def upload_stand(request):
    if request.method == 'POST':
        form = StandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stand_list')
    else:
        form = StandForm()
    return render(request, 'upload_stand.html', {'form': form})

def stand_list(request):
    stands = Stand.objects.all()
    paginator = Paginator(stands, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'stand_list.html', {'page_obj': page_obj})
