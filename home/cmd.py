
"""from .models import Person,Attendance,Student

#list1=Person.objects.bulk_create([    
    #Person(user="Rohan",attendance=32),
    #Person(user="Nitin",attendance=23)
    
#])
raghav_student = Student.objects.get(user__username="raghav")
attendance_data = Attendance.objects.bulk_create([
    Attendance(student=raghav_student, date='2024-03-20', status="Present"),
    Attendance(student=raghav_student, date='2024-03-21', status="Present"),
])"""