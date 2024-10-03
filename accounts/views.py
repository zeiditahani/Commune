from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

# Create your views here.
#def accounts(request):
   #template = loader.get_template('commune/registration/login.html')
 #  return render(request, 'registration/login.html')
class SignUpView(CreateView):#new class called SignUpView that extends CreateView sets the form as UserCreationForm, and uses the not-yet-created template signup.html.
    form_class = UserCreationForm
    success_url = reverse_lazy("login")#we use reverse_lazy to redirect users to the login page upon successful registration rather than reverse, because for all generic class-based views, the URLs are not loaded when the file is imported, so we have to use the lazy form of reverse to load them later when we are sure they're available.
    template_name = "registration/signup.html"
# Create your views here.
