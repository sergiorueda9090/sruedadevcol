from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'business', 'phone', 'service', 'source', 'created_at')
    list_filter = ('service', 'source', 'created_at')
    search_fields = ('name', 'business', 'phone')
    readonly_fields = ('created_at', 'user_agent', 'ip')
