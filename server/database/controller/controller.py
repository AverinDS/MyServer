from django.http import HttpResponse, JsonResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from ..view import work_with_DB as DB
from ..view.serializers.SerializerShop import SerializerShop
from ..view.serializers.SerializerProduct import SerializerProduct
from ..view.serializers.SerializerComment import SerializerComment
import json


# it's method for checking
def index(request):
    return HttpResponse("Congratulations! It is index page!")


# GET
def select_all(request):
    return JsonResponse(SerializerShop(DB.select_all_Shop(), many=True).data, safe=False)


# GET
def select_product_from_shop(request, shopId):
    return JsonResponse(SerializerProduct(DB.select_products_from_shop(shopId), many=True).data, safe=False)


# GET
def get_comments_to_shop(request, shopId):
    return JsonResponse(SerializerComment(DB.get_comments_about_shop(shopId), many=True).data, safe=False)


# POST
@csrf_exempt
def create_comment(request):
    json_data = json.loads(request.POST.get('comment'))
    comment = json_data[0]['commentLine']
    rate = json_data[0]['rate']
    id_shop = json_data[0]['shopFK']
    return HttpResponse(DB.create_comment(commentOfUser=comment, rateUser=rate, idShop=id_shop))

# POST
@csrf_exempt
def update_comment(request):
    json_data = json.loads(request.POST.get('comment'))
    id_shop = json_data[0]['id']
    comment = json_data[0]['commentLine']
    rate = json_data[0]['rate']
    id_shop = json_data[0]['shopFK']
    return HttpResponse(DB.update_comment(idComment=id_shop, newRate=rate, newComment=comment))


# POST
@csrf_exempt
def delete_comment(request):
    json_data = json.loads(request.POST.get('comment'))
    id_comment = json_data[0]['id']
    return HttpResponse(DB.delete_comment(idComment=id_comment))
