from django.contrib import admin

from .models import Attendance,Person,Student

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Person)
