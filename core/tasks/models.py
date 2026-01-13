from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']


class TaskStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Alert(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
import uuid

class Task(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=100)
    date_end = models.DateField()
    assigned_to = models.ForeignKey(CustomUser, related_name='tasks_assigned', on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(TaskStatus, related_name='tasks', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    alerts = models.ManyToManyField(Alert, related_name='tasks', blank=True)
    created_by = models.ForeignKey(CustomUser, related_name='tasks_created', on_delete=models.CASCADE, null=True)
    objective = models.TextField()
    percent = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def save(self, *args, **kwargs):
        if not self.pk:
            user = kwargs.pop('user', None)
            if user:
                self.created_by = user
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
