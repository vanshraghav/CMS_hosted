from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ['tracking_id', 'sender_name', 'receiver_name', 'Current_Status']
    list_filter = ['Current_Status']
    search_fields = ['tracking_id', 'sender_name', 'receiver_name']

    actions = ['mark_as_completed', 'mark_as_pending']

    def mark_as_completed(self, request, queryset):
        queryset.update(Current_Status='Delivered')

    mark_as_completed.short_description = 'Mark selected bookings as Delivered'

    def mark_as_pending(self, request, queryset):
        queryset.update(Current_Status='In transit')

    mark_as_pending.short_description = 'Mark selected bookings as In Transit'

admin.site.register(Booking, BookingAdmin)





