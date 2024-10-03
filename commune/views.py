from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from commune.form import ReclamationForm
from commune.models import Reclamation

# Create your views here.
def reclamation(request):
  if request.method == 'POST':
    form = ReclamationForm(request.POST)
    if form.is_valid():
      form.save()
      obj=Reclamation.objects.all()
      context={ "obj":obj,}
      return render(request,'home.html', context)
  else:
    form = ReclamationForm()
  print("Rendering form.")
  return render(request, 'reclamation.html', {'form': form})




def index(request):
  obj=Reclamation.objects.all()
  context={ "obj":obj,}
  return render(request,'home.html', context)
def home(request):
  obj=Reclamation.objects.all()
  context={ "obj":obj,}
  return render(request,'home.html', context)