from django.shortcuts import render , HttpResponse
from django.views.decorators.csrf import csrf_exempt
from class_app.models import Clas
from teacher_app.models import Teacher
import json


def class_list(request):
    clases = Clas.objects.all()
    class_list  = []
    for item in clases:
        class_dict = {
            "name": item.name,
            "time" : item.time,
            'price ': item.price,
            'category' : item.category
            
        }
        class_list.append(class_dict)
    return HttpResponse (class_list)


@csrf_exempt
def create_class(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        selected_tacher = Teacher.objects.get(id=body['input_cupon'])
        Clas.objects.create(
            name= body['input_name'],
            price= body['input_price'],
            time = body['input_class'],
            category= body['input_category'],
            teacher = selected_tacher
        )
        return HttpResponse("new class reserved and factor made")
    else:
        return HttpResponse("BAD REQUEST")
    

@csrf_exempt
def update_price(request , inp_id):
    if request.method == 'PATCH':
        body = json.loads(request.body)
        item = Clas.objects.get(id = inp_id)
        item.price = body['input_price']
        item.save()
        return HttpResponse("price updated!")
    else:
        return HttpResponse("BAD REQUEST")