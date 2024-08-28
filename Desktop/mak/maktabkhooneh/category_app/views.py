from django.shortcuts import render
from django.http.response import HttpResponse , JsonResponse
from category_app.models import Category
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def search_category(request):
    if request.method == "POST" :
        body = json.loads(request.body)
        category = Category.objects.get(id=body["category_inp"])
        category_lst = Category.objects.all()
        lst = []
        for i in category_lst :
            if i == category :
                lst.append(i)
            return JsonResponse(lst , safe= False)

def return_all_categorys(request) :
    category = Category.objects.all()
    lst = []
    for i in category :
        lst.append(i)
    return JsonResponse(lst , safe= False)
# Create your views here.
