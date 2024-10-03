from django.contrib import admin
from commune.models import Reclamation

class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'numTel', 'email', 'sujet', 'adresseGoogle', 'photo')

# Register your models here.
admin.site.register(Reclamation, ReclamationAdmin)