from django.shortcuts import render , HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cupon_app.models import Cupon
from factor_app.models import Factor
import json


def calculate_price(request):
    factors = Factor.objects.all()
    for items in factors:
        items.price = items.price - (items.price * items.cupon.percent /100)
        items.price.save()

@csrf_exempt
def create_factor(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        selected_cupon = Cupon.objects.get(id=body['input_cupon'])
        Factor.objects.create(
            student_name= body['input_name'],
            price= body['input_price'],
            class1 = body['input_class'],
            cupon = selected_cupon
        )
        return HttpResponse("new class reserved and factor made")
    else:
        return HttpResponse("BAD REQUEST")
        
# Create your views here.
