from django.contrib import admin
from .models import Employee
from .models import Developer
from .models import Devdetails
from .models import Employeedetails
from .models import EmployeeInfo

# Register your models here.
admin.site.register(Employee)
admin.site.register(Developer)
admin.site.register(Devdetails)
admin.site.register(Employeedetails)
admin.site.register(EmployeeInfo)
