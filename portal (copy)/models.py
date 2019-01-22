from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    date_of_joining = models.DateField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def pending_tasks(self):
        return self.task_set.filter(submitted=False).count()

    def completed_tasks(self):
        return self.task_set.filter(submitted=True).count()


class Task(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    issued_on = models.DateField(auto_now=True)
    start_date = models.DateField()
    deadline = models.DateField()
    submitted = models.BooleanField(default=False)
    submitted_on = models.DateField(blank=True, null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return '{0} -->> {1}'.format(self.name, self.employee.name)
