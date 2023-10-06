from operator import ge
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from collegeapp.models import CourseModel, teacherModel,StudentModel



def open_main(request):
    return render(request,'main.html')

def open_signup(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'signup.html',context)

def open_course(request):
    return render(request,'addcourse.html')

@login_required(login_url='login')
def addstu(request):
    courses=CourseModel.objects.all()
    return render(request,'addstudent.html',{'courses':courses})

def tstudent(request):
    student_detail = StudentModel.objects.all()
    return render(request,'tstudent.html',{'student':student_detail})

def open_signin(request):
    return render(request,'signin.html')   

@login_required(login_url='login')
def teacherpage(request):
    return render(request,'teacherpage.html') 

@login_required(login_url='login')
def adminpage(request):
    return render(request,'admin.html') 

def tprofile(request,pk):
    tdetail = User.objects.get(id=pk)
    teach=teacherModel.objects.get(Teacher=pk)
    return render(request,'tprofile.html',{'detail':tdetail,'teach':teach})

def tedit(request,pk):
    tdetail = User.objects.get(id=pk)
    teach=teacherModel.objects.get(Teacher=pk)
    return render(request,'edit.html',{'detail':tdetail,'teach':teach})
   
def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        address=request.POST['address']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        gender=request.POST['gender']
        age=request.POST['age']
        image=request.FILES['choose-file']

        if password==cpassword: 
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('open_signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                    )
                user.save()
                teacher=User.objects.get(username=username)
                data =teacherModel(Teacher_Address=address,Teacher_Gender=gender,Teacher_Age=age,Teacher_Photo=image,Teacher=teacher)
                data.save()
                messages.success(request, "Registered successfully")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('open_signup')   
        return redirect('open_signup')            

def edit_profile(request,pk):    
    if request.method=='POST':
        user = User.objects.get(id=pk)
        teach=teacherModel.objects.get(Teacher=pk)
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        teach.Teacher_Address=request.POST.get('address')
        teach.Teacher_Gender=request.POST.get('gender')
        teach.Teacher_Age=request.POST.get('age')
        user.email = request.POST.get('email')
        user.username = request.POST.get('uname')
        if request.FILES.get('file') is not None:
            teach.Teacher_Photo=request.FILES.get('file')
        else:
            teach.Teacher_Photo=teach.Teacher_Photo
        user.save()
        teach.save()
        return redirect('tprofile',pk=user.id)
    return render(request, 'Edit.html',)
    
@login_required(login_url='login')
def Addcourse(request):
    if request.method == 'POST':
        coursename=request.POST['coursename']
        coursefees=request.POST['coursefees']
        data = CourseModel(Course_Name=coursename,Course_Fees=coursefees)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('tcourse')

def addstudent(request):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['jdate']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
        data = StudentModel(Std_Name=name,Std_Address=address,Std_Age=age,Join_Date=jdate,Course=course)
        data.save()
        return redirect('tstudent')


def tcourse(request):
        course=CourseModel.objects.all()
        return render(request,'tcourse.html',{'cdata':course})   

def dteacher(request):
        teach=teacherModel.objects.all()
        return render(request,'dteacher.html',{'tdata':teach})                

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user1=auth.authenticate(username=username,password=password)
        if user1 is not None:
            if user1.is_staff:
                auth.login(request,user1)
                return redirect('adminpage')
            else:
                auth.login(request,user1)
                messages.info(request,f'welcome {username}')
                return redirect('teacherpage')
        else:
            messages.info(request,'Invalid Username or Password.Try Again')
            return redirect('open_signin')
    else:
        return redirect('open_signin')                


def logout(request):
	auth.logout(request)
	return redirect('signin')