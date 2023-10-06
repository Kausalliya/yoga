from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=70)
    Course_Fees=models.IntegerField()

class StudentModel(models.Model):
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    Std_Name=models.CharField(max_length=100)
    Std_Address=models.CharField(max_length=200)
    Std_Age=models.IntegerField()
    Join_Date=models.DateField(auto_now_add=True)

class teacherModel(models.Model):
    Teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    Teacher_Address=models.CharField(max_length=100)
    Teacher_Gender=models.CharField(max_length=10)
    Teacher_Age=models.IntegerField()
    Teacher_Photo=models.ImageField(blank=True,upload_to='image/',default='static/image/default.png')

    # def __str__(self):
    #     return self.Std_Name