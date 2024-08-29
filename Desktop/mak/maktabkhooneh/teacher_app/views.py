from django.http.response import HttpResponse, JsonResponse
from teacher_app.models import Teacher
from django.views.decorators.csrf import csrf_exempt
import json


def teacher_list(request):
    all_teachers = Teacher.objects.all()
    my_teacher_list = []
    for teacher in all_teachers:
        teacher_dictionary = {
            "first name" : teacher.first_name,
            "last name" : teacher.last_name,
            "email" : teacher.email,
            "phone number " : teacher.phone_number,
            "clas" : teacher.clas,
            # "category" : teacher.category,
            "rate" : teacher.rate,
            "wallet" : teacher.wallet
        }
        my_teacher_list.append(teacher_dictionary)
    return JsonResponse(my_teacher_list , safe=False)


@csrf_exempt
def signup(request) :
    if request.method == 'POST' :
        body = json.loads(request.body)
        Teacher.objects.create(
            name= body['name_inp'] , 
            email = body['email_inp'] , 
            phone_number = body['phone_number_inp'] ,
        )
        return HttpResponse("new user added")
    else : 
        return HttpResponse("bad request!")

    
@csrf_exempt  
def average_rate(request):  
    if request.method == 'GET':  
        all_teachers = Teacher.objects.all()
        if not all_teachers:  
            return JsonResponse({"average_rate": 0})  
        total_rate = sum(teacher.rate for teacher in all_teachers)
        average = total_rate / len(all_teachers)  
        return JsonResponse({"average_rate": average})  
    else:  
        return HttpResponse("bad request!", status=400)


@csrf_exempt
def sort_by_rate(request):
    if request.method == 'GET':
        all_teachers = Teacher.objects.all()
        sorted_list = sorted(all_teachers, key=lambda teacher: teacher.rate, reverse=True)
        my_teacher_list = []
        for teacher in sorted_list:
            teacher_dictionary = {
                "first name" : teacher.first_name,
                "last name" : teacher.last_name,
                "email" : teacher.email,
                "phone number " : teacher.phone_number,
                "clas" : teacher.clas,
                # "category" : teacher.category,
                "rate" : teacher.rate,
                "wallet" : teacher.wallet
            }
            my_teacher_list.append(teacher_dictionary)
        return JsonResponse(my_teacher_list , safe=False)
    else:
        return HttpResponse("bad request!")
        