from django.contrib import admin

from collegeapp.models import CourseModel,StudentModel,teacherModel

# Register your models here.
@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course_Name','Course_Fees')

@admin.register(StudentModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course','Std_Name','Std_Address','Std_Age','Join_Date')

@admin.register(teacherModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','Teacher','Course','Teacher_Address','Teacher_Gender','Teacher_Age','Teacher_Photo')    