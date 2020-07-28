from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sex', 'phone', 'location')
    list_filter = ('time_stamp',)
    search_fields = ('first_name', 'first_name', 'location')
    ordering = ('time_stamp',)

