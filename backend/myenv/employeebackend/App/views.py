from rest_framework import status
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .models import Developer
from .models import Devdetails
from .models import EmployeeInfo
from .serializers import DataSerializer
from .serializers import EmployeeDetailsSerializer
from .serializers import DeveloperDetailsSerializer
from .serializers import EmployeeSerializer
from .serializers import DeveloperSerializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from django.core.mail import send_mail
import json

# Create your views here.http://127.0.0.1:8000//api/employeedataall/
def index(request):
    data={
        'ai':'hi'
    }
    return JsonResponse(data)


# @api_view(['GET'])
# def developerdetails(request,pk):
#     info=Devdetails.objects.get(dev_id=pk)
#     serializer=DataSerializer(info,many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def alldeveloperdetails(request):
#     info=Devdetails.objects.all()
#     serializer=DataSerializer(info,many=True)
#     return Response(serializer.data)





@api_view(['POST'])
def employee_signup(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def employee_login(request):
    employee_id = request.data.get('employeeid')
    password = request.data.get('password')
    try:
        employee = get_object_or_404(Employee, employee_id=employee_id, password=password)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def developer_signup(request):
    serializer = DeveloperSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def developer_login(request):
    employee_id = request.data.get('employeeid')
    password = request.data.get('password')
    try:
        employee = get_object_or_404(Developer, employee_id=employee_id, password=password)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



# @api_view(['POST'])
# def employee_form(request):
#     serializer = EmpSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def products(request):
    product=[
    {
        'name': 'sai',
        'age': 20,
        'place': 'hyd'
    },
    {
        'name': 'sai2',
        'age': 19,
        'place': 'chennai'
    },
    {
        'name': 'sai3',
        'age': 18,
        'place': 'banglore'
    },
    ]
    return Response(product)


@api_view(['POST'])
def devdetails(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def employeeinfo(request):
    serializer = EmployeeDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeInfoDetailView(generics.RetrieveAPIView):
    queryset = EmployeeInfo.objects.all()
    serializer_class = EmployeeDetailsSerializer
    lookup_field = 'employeeId'


class DevloperInfoDetailView(generics.RetrieveAPIView):
    queryset = Devdetails.objects.all()
    serializer_class = DeveloperDetailsSerializer
    lookup_field = 'dev_id'


from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

class Sendmail(APIView):
    def post(self, request):
        try:
            data = request.data
            employee_id = data.get('employeeId')
            company_email = data.get('companyEmail')
            password = data.get('password')
            recipient_email = data.get('companyEmail')  # Assuming companyEmail is the recipient's email

            # Compose the email subject and message
            subject = 'Employee Details'
            message = f'Employee ID: {employee_id}\nCompany Email: {company_email}\nPassword: {password}'
            sender_email = settings.EMAIL_HOST_USER

            # Send the email
            send_mail(subject, message, sender_email, [recipient_email])

            # Return success response
            return Response({'status': True, 'message': 'Email sent successfully'})
        except Exception as e:
            # Return error response if there's an exception
            return Response({'status': False, 'message': str(e)}, status=500)


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            employee_id = data['employeeId']
            company_email = data['companyEmail']
            password = data['password']

            send_mail(
                'Employee ID and Password',
                f'Employee ID: {employee_id}\nPassword: {password}',
                settings.EMAIL_HOST_USER
                [company_email],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
