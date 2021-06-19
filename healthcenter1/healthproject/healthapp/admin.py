from django.contrib import admin
from .models import Doctor, Appointment, Department,DoctorList

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Appointment)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)

class DoctorListAdmin(admin.ModelAdmin):
    list_display = ['name','slug','phnno']
    list_editable = ['phnno']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(DoctorList,DoctorListAdmin)
