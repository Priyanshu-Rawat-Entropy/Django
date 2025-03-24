from django.contrib import admin
from .models import TimeSlot, TimeSlotRequest
# Register your models here.

class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(TimeSlot)
admin.site.register(TimeSlotRequest)