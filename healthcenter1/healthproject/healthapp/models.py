from django.db import models
from django.urls import reverse

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    spec = models.CharField(max_length=250)
    desc = models.TextField()
    mail = models.EmailField()
    phnno = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=250,unique=True)
    img = models.ImageField(upload_to='department',blank=True)
    slug = models.SlugField(max_length=250,unique=True)
    desc = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse('healthapp:doclist_by_department',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class DoctorList(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    img = models.ImageField(upload_to='departmentlist',blank=True)
    desc = models.TextField(blank=True)
    mail = models.EmailField(blank=True)
    phnno = models.CharField(max_length=12)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)


    class Meta:
        ordering = ('name',)
        verbose_name = 'doctorlist'
        verbose_name_plural = 'doctorlists'

    def get_url(self):
        return reverse('healthapp:doclistdetail', args=[self.department.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)



class Appointment(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.CharField(max_length=250)
    message = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
