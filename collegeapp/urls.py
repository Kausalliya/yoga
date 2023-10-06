from django.urls import path
from .import views

urlpatterns = [
   path('',views.open_main,name='open_main'),
   path('open_signup',views.open_signup,name='open_signup'),
   path('open_signin',views.open_signin,name='open_signin'),
   path('teacherpage',views.teacherpage,name='teacherpage'),
   path('adminpage',views.adminpage,name='adminpage'),
   path('register',views.register,name='register'),
   path('Addcourse',views.Addcourse,name='Addcourse'),
   path('addstu',views.addstu,name='addstu'),
   path('tcourse',views.tcourse,name='tcourse'),
   path('addstudent',views.addstudent,name='addstudent'),
   path('tstudent',views.tstudent,name='tstudent'),
   path('dteacher',views.dteacher,name='dteacher'),
   path('open_course',views.open_course,name='open_course'),
   path('login',views.login,name='login'),
   path('logout',views.login,name='logout'),
   path('tprofile/<int:pk>',views.tprofile,name='tprofile'),
   path('tedit/<int:pk>',views.tedit,name='tedit'),
   path('edit_profile/<int:pk>',views.edit_profile,name='edit_profile'),
   
  ]
