from django.urls import path 
from . import views
from .views import EmployeeInfoDetailView
from .views import DevloperInfoDetailView
from .views import Sendmail

urlpatterns = [
    path('',views.index,name='index'),
    path('products/',views.products,name='products'),
    # path('devdataall/',views.alldeveloperdetails,name='devdataall'),
    # path('devdata/<str:pk>',views.developerdetails,name='devdata'),
    # path('employeedataall/',views.allemployeedetails,name='empdata'),
    path('employees/signup/', views.employee_signup, name='employee_signup'),
    path('employees/login/', views.employee_login, name='employee_login'),
    path('developers/signup/', views.developer_signup, name='developer_signup'),
    path('developer/login/', views.developer_login, name='developer_login'),
    # path('employeeinfo', views.employee_form, name='employee_info'),
    path('devdetails/', views.devdetails, name='devdetails'),
    path('employeeinfo/', views.employeeinfo, name='employee_info'),
    path('employee/<str:employeeId>/', EmployeeInfoDetailView.as_view(), name='employee-detail'),
    path('developer/<str:dev_id>/', DevloperInfoDetailView.as_view(), name='developer-detail'),
    # path('send-email/', views.send_email, name='send_email'),
    path('sendemail/',Sendmail.as_view())
]
