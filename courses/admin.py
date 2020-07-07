from django.contrib import admin
from courses.models import Subject, Course

# Register your models here.


@admin.register(Subject)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    prepopulated_fields = {'slug': ('title',)}
