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
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField(validators=[
        RegexValidator(
            regex=mobile_number_regex,
            message="Mobile number must be exactly 10 digits.",
        ),
    ], blank=True, null=True)
    date_of_birth = models.DateField()
    role = models.CharField(max_length=50, choices=USER_ROLES)
    department = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    heading = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    eta = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='task_created')
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='task_assigned')

    def clean(self):
        if self.created_by.role != 'manager' or self.assigned_to.role != 'developer':
            raise ValidationError("Only managers can assign tasks to developers.")

    def __str__(self):
        return 'Task - {},'.format(self.heading) + ' Assigned to {}'.format(self.assigned_to.user.username)
