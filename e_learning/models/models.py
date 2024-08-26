from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError
from django.utils import timezone


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user
    

class Skills(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    # LEVELS = [
    #     ('beginner', 'Beginner'),
    #     ('intermediate', 'Intermediate'),
    #     ('advanced', 'Advanced'),
    # ]
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True, max_length=1000)
    # industry = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images/', editable=True, null=True)
    start_date = models.DateField()
    duration = models.CharField(max_length=1000, null=True)
    level = models.ForeignKey(Level, max_length=255, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def clean(self):
        # Ensure the start date is in the future
        if self.start_date <= timezone.now().date():
            raise ValidationError("The start date cannot be today or in the past.")
        

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    resource = models.FileField(upload_to='lesson_documents/', null=True, blank=True, validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
        ])

    def __str__(self):
        return self.name


class CourseDetails(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    about = models.TextField(max_length=10000)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.name}"