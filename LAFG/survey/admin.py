from django.contrib import admin

from .models import Survey, Survey_Key


@admin.register(Survey)
class PersonAdmin(admin.ModelAdmin):
    # list_display = ('id',)
    pass

@admin.register(Survey_Key)
class PersonAdmin(admin.ModelAdmin):
    # list_display = ('id',)
    pass


# @admin.register(Survey)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('time_stamp', 'first_name', 'last_name', 'sex', 'age', 'phone', 'location', 'source')
#     list_filter = ('time_stamp',)
#     search_fields = ('first_name', 'first_name', 'location')
#     ordering = ('-time_stamp',)
