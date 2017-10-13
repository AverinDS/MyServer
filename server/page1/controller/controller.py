from django.http import HttpResponse, JsonResponse
from ..models.Shop import Shop
from ..models.Product import Product
from ..models.Comment import Comment
from ..view import work_with_DB as DB
from ..view.serializers.SerializerShop import SerializerShop
from ..view.serializers.SerializerProduct import SerializerProduct
from ..view.serializers.SerializerComment import SerializerComment




#it's for checking
def index(request):
    return HttpResponse("Congratulations! It is index page!")


def select_all(request):
    return JsonResponse(SerializerShop(DB.select_all_Shop(), many=True).data, safe=False)


def select_shop_town(request, town):
    shops = ""


def select_product_from_shop(request, shopId):
    return JsonResponse(SerializerProduct(DB.select_products_from_shop(shopId), many=True).data, safe=False)


def get_comments_to_shop(request, shopId):
    return JsonResponse(SerializerComment(DB.get_comments_about_shop(shopId), many=True).data, safe=False)


def update_comment(request, shopId, newLine):
    c = ""


def delete_comment(request, shopId, line ):
    c = ""


# def create_comment(request, shopId, line, rate_user):
#     comment = Comment(rate=rate_user, commentLine=line, shopFK=shopId)
#     try:
#         comment.save()
#         return HttpResponse("success", status=200)
#     except():
#         return HttpResponse("fail", status=500)


