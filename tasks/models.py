from django.db import models
from django.core.exceptions import ValidationError

from users.models import Employee


# Create your models here.
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
