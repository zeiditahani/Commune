"""project_commune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from commune import views
from django.views.generic.base import TemplateView  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reclamation/',views.reclamation),
    path('acceuil/',views.index),
    path("",views.home),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new
    path("acceuil/", TemplateView.as_view(template_name="acceuil.html"), name="acceuil"),
    path("reclamation", TemplateView.as_view(template_name="reclamation.html"), name="reclamation"),
]
