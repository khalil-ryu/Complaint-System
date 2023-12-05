from django.contrib import admin
from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'encrypted_title', 'encrypted_description', 'created_at')

admin.site.register(Complaint, ComplaintAdmin)