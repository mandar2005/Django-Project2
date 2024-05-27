from django.urls import path
from .views import  login_view
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path('login/', login_view, name='login'),
    path("private/", views.private, name="private"),
    path("about/", views.about, name="about"),
    path("attend/", views.attend, name="attend"),
    path("attendance/", views.attendance, name="attendance"),
    path("logout/", views.logout_view, name="logout"),
    path("signin/", views.signin, name="signin"),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path("add_person/", views.add_person, name="Add Person"),
    
]