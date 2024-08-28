from django.http.response import HttpResponse, JsonResponse
from cupon_app.models import Cupon


def cupon_list(request):
    all_cupons = Cupon.objects.all()
    my_cupon_list = []
    for cupon in all_cupons:
        cupon_dictionary = {
            "title": cupon.title,
            "expire_date": cupon.expire_date,
            "percent": cupon.percent,
            "cupon availablity": cupon.cupon_availability,
        }
        my_cupon_list.append(cupon_dictionary)

    return JsonResponse(my_cupon_list,safe=False)