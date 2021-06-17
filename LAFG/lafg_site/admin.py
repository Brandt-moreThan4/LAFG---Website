from django.contrib import admin
from .models import Person, Place, State, Faq


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('time_stamp', 'first_name', 'last_name', 'sex', 'age', 'phone', 'zip', 'source')
    list_filter = ('time_stamp',)
    search_fields = ('first_name', 'first_name', 'zip')
    ordering = ('-time_stamp',)


@admin.register(Place)
class PlacedAdmin(admin.ModelAdmin):
    # list_display = ('city_value', 'state', 'display')
    list_display = ('city_value', 'display')


@admin.register(State)
class PlacedAdmin(admin.ModelAdmin):
    list_display = ('name', 'display')

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')