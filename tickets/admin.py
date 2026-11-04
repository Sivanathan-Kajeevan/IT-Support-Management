from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'category',
        'priority',
        'status',
        'created_by',
        'created_at'
    )

    list_filter = (
        'category',
        'priority',
        'status'
    )

    search_fields = (
        'title',
        'description'
    )

    list_editable = (
        'status',
    )