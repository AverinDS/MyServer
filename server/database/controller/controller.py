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
    return HttpResponse(DB.create_comment(commentOfUser=json_data[0]['commentLine'], rateUser=json_data[0]['rate'],
                                          idShop=json_data[0]['shopFK']))


# POST
# !DON'T WORK
def update_comment(request):
    idComment = request.POST.get('idComment')
    newRate = request.POST.get('newRate')
    newBodyOfComment = request.POST.get('newComment')

    return JsonResponse(SerializerComment(DB.update_comment(idComment, newRate, newBodyOfComment), many=False).data,
                        safe=False)


# POST
# !DON'T WORK
def delete_comment(request):
    idComment = request.POST.get('idComment')
    DB.delete_comment(idComment)
    return HttpResponse("Success")
