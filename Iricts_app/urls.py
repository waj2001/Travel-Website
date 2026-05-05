from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.login, name="signin"),
    path('signout/',views.signout,name="signout"),
    path('calc/',views.calculator),
    path('calc/add',views.add),
    path('calc/sub',views.sub),
    path('calc/mult',views.mult),
    path('calc/div',views.div),
   
]
