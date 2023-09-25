from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Employee(models.Model):
    DEVELOPER = 'developer'
    MANAGER = 'manager'
    USER_ROLES = [
        (DEVELOPER, 'Developer'),
        (MANAGER, 'Manager'),
    ]
    mobile_number_regex = r'^\d{10}$'

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True,blank=True)
    contact_no = models.IntegerField(validators=[
        RegexValidator(
            regex=mobile_number_regex,
            message="Mobile number must be exactly 10 digits.",
        ),
    ], blank=True, null=True)
    date_of_birth = models.DateField(null=True,blank=True)
    role = models.CharField(max_length=50, choices=USER_ROLES,null=True,blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username



