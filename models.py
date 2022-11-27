from django.db import models


class Employee(models.Model):
    regid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return f'{self.regid}--{self.name}'


class EmployeeAddress(models.Model):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeAddress')
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.employee.regid}--{self.employee.name}'


class EmployeeWorkExperience(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeWorkExperience')
    companyName = models.CharField(max_length=100)
    fromDate = models.CharField(max_length=100)
    toDate = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.employee.regid}--{self.employee.name}'


class EmployeeQualification(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeQualification')
    qualificationName = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.employee.regid}--{self.employee.name}'


class EmployeeProjects(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeProjects')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.employee.regid}--{self.employee.name}'
