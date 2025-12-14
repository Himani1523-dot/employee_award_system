from django.contrib import admin
from .models import Employee, AwardCategory, Award


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "department", "position", "joining_date")
    list_filter = ("department", "position")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("joining_date",)                           #order by joining date

class AwardCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",'description')    
    search_fields = ("title",)

#@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("employee", "category", "date_given")
    list_filter = ("category", "date_given")
    search_fields = ("employee__first_name", "employee__last_name", "category__title")
    ordering = ("-date_given",)                      #minus(descending order) on date given of award was given 


# Registering models here.
admin.site.register(Employee, EmployeeAdmin)         #here we register our model.py class name and after that we register ourr custom made admin class name.
admin.site.register(AwardCategory, AwardCategoryAdmin)
admin.site.register(Award, AwardAdmin)

"""there is also another way to register model without custom admin class like below:
=====> admin.site.register(AwardCategory) <====== #this is default way to register model without custom admin class. but here we cannot customize how we want to see that model in admin panel."""
""" one more way is to use decorator like:
@admin.register(Award)"""


