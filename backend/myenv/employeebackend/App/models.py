from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    employee_id = models.CharField(max_length=70, primary_key=True)
    password = models.CharField(max_length=70) 
    def __str__(self):
        return f"Employee ID: {self.employee_id}"

class Developer(models.Model):
    employee_id = models.CharField(max_length=70, primary_key=True)
    password = models.CharField(max_length=70) 
    def __str__(self):
        return f"Employee ID: {self.employee_id}"
    

class Devdetails(models.Model):
    dev_id = models.CharField(max_length=10, primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=11)
    dateofbirth = models.DateField()
    designation = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='developer_photos/')
    experience = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    
class Employeedetails(models.Model):
    emp_id=models.CharField(max_length=11,primary_key=True)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"
    


class EmployeeInfo(models.Model):
    employeeId = models.CharField(max_length=10, primary_key=True)
    photo = models.ImageField(upload_to='photos/')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    homeAddress = models.TextField()
    phoneNumber = models.CharField(max_length=11)
    emailAddress = models.EmailField(max_length=50)
    jobTitle = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    startDate = models.DateField()
    employmentType = models.CharField(max_length=20)
    workLocation = models.CharField(max_length=50)
    degreememo = models.FileField(upload_to='documents/')
    sscmemo = models.FileField(upload_to='documents/')
    idcard = models.FileField(upload_to='documents/')
    resume = models.FileField(upload_to='documents/')
