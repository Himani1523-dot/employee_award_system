from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employees_list, name='employees'),
    path('awards/', views.awards_list, name='awards'),
    path('give-award/', views.give_award, name='give_award'),
    path("add-employee/", views.add_employee, name="add_employee"),

]
