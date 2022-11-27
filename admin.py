from django.contrib import admin
from .models import EmployeeQualification, EmployeeWorkExperience, EmployeeAddress, Employee, EmployeeProjects


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('regid', 'name', 'email', 'age',
                    'gender', 'phoneNo', 'photo')


@admin.register(EmployeeAddress)
class EmployeeAddressAdmin(admin.ModelAdmin):
    list_display = ('employee', 'hno', 'street', 'city', 'state', )


@admin.register(EmployeeWorkExperience)
class EmployeeWorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'companyName',
                    'fromDate', 'toDate', 'address', )


@admin.register(EmployeeQualification)
class EmployeeQualificationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'qualificationName', 'percentage', )


@admin.register(EmployeeProjects)
class EmployeeProjectsAdmin(admin.ModelAdmin):
    list_display = ('employee', 'title', 'description', )
