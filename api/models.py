from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.db import models

class Department(models.Model):
    role = models.CharField(max_length=128)
    def __str__(self):
        return self.role
    

class Staff(models.Model):
    name = models.CharField(max_length=128,null=False, blank=False, verbose_name="Full Name")
    card_id = models.CharField(max_length=128,null=False, blank=False, verbose_name="Card ID", unique=True)
    phone_number = PhoneNumberField(blank=True,null=True,unique=True, verbose_name="Phone Number")
    email = models.EmailField(max_length=128, null=False, blank=False, verbose_name="Gmail", unique=True )
    gender = models.CharField(max_length=10 ,choices=[('Male', 'Male'), ('Female', 'Female')], verbose_name="Gender")
    department = models.ForeignKey(Department, related_name='staff_department', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Record(models.Model):
    staff = models.ForeignKey(Staff, related_name='record_staff', on_delete=models.SET_NULL, null=True, verbose_name="Staff")
    datetime = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name="Time")
    action = models.CharField(max_length=100, choices=[("in", 'In'), ('out', 'Out')])

    @property
    def name(self):
        return self.staff.name
    
    @property
    def card_id(self):
        return self.staff.card_id
    
    @property
    def phone_number(self):
        return self.staff.phone_number
    
    @property
    def email(self):
        return self.staff.email
    
    @property
    def gender(self):
        return self.staff.gender
    
    @property
    def department(self):
        return self.staff.department
    
    @property
    def user(self):
        return self.staff.user

class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")