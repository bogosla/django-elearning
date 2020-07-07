from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='courses_joined', blank=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.title