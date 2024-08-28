from django.shortcuts import render 
from django.http.response import HttpResponse , JsonResponse
from class_app.models import Class
from student_app.models import Student
import json
from django.views.decorators.csrf import csrf_exempt

def return_all_students(request):
    student_lst = Student.objects.all()
    lst = []
    for i in student_lst :
        lst.append(i) 
    return JsonResponse(lst , safe= False)

def list_class(request , student_name) :
    Class_lst = Class.objects.filter(student= student_name).values('name' , 'time' , 'price' , 'teacher' , 'category')
    return JsonResponse(list(Class_lst) , safe= False)

@csrf_exempt
def signup(request) :
    if request.method == 'POST' :
        body = json.loads(request.body)
        Student.objects.create(
            name= body['name_inp'] , 
            email = body['email_inp'] , 
            phone_number = body['phone_number_inp'] ,
        )
        return HttpResponse("new user added")
    else : 
        return HttpResponse("bad request!")

def payment(request) :
    pass
# Create your views here.
