from django.contrib import admin
from . import models
from django.utils.html import format_html


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):

    list_display = ["employee_id","firstname","department"]

admin.site.register(models.Client)
admin.site.register(models.Course)
admin.site.register(models.Department)
admin.site.register(models.Employee,EmployeeAdmin)
admin.site.register(models.Project)

admin.site.register(models.AsessmentBank)
admin.site.register(models.Badge)
# admin.site.register(models.Certificate)
admin.site.register(models.Compitency)
admin.site.register(models.Design_Request)
# admin.site.register(models.Visa)
admin.site.register(models.Task)
admin.site.register(models.Simulation)
admin.site.register(models.Facilitator)
admin.site.register(models.Idea)
admin.site.register(models.Inventory)
admin.site.register(models.Logestics)
# admin.site.register(models.Material)
admin.site.register(models.Portfolio)
# admin.site.register(models.Flight)
# admin.site.register(models.Hotel_of_course)
admin.site.register(models.Manager)
# admin.site.register(models.Trainers_hotel)
admin.site.register(models.Repository)
admin.site.register(models.Notification)
admin.site.register(models.Comments)
admin.site.register(models.Invoice)
admin.site.register(models.Contract)


