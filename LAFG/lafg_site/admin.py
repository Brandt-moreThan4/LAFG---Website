from django.contrib import admin
from .models import Person, Place, State


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('time_stamp', 'first_name', 'last_name', 'sex', 'age', 'phone', 'location', 'source')
    list_filter = ('time_stamp',)
    search_fields = ('first_name', 'first_name', 'location')
    ordering = ('-time_stamp',)


@admin.register(Place)
class PlacedAdmin(admin.ModelAdmin):
    # list_display = ('city_value', 'state', 'display')
    list_display = ('city_value', 'display')


@admin.register(State)
class PlacedAdmin(admin.ModelAdmin):
    # list_display = ('city_value', 'state', 'display')
    list_display = ('name', 'display')