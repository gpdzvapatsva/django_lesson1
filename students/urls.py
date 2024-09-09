from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="students-home"),
    path('about/', views.about, name="students-about"),
    path('skills/', views.skills, name="students-skills"),
]


