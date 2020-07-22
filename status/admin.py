from django.contrib import admin
from .forms import StatusForm
from .models import Status as StatusModel


class StatusAdmin(admin.ModelAdmin):
    # Show only specified fields in list view of Status in admin view:
    list_display = ['user', '__str__', 'image']

    # For validation:
    form = StatusForm


admin.site.register(StatusModel, StatusAdmin)
