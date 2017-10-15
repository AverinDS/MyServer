from django.http import HttpResponse, JsonResponse
from ..view import work_with_DB as DB
from ..view.serializers.SerializerShop import SerializerShop
from ..view.serializers.SerializerProduct import SerializerProduct
from ..view.serializers.SerializerComment import SerializerComment


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
def create_comment(request):
    bodyComment = request.POST.get('bodyComment')
    rate = request.POST.get('rate')
    idShop = request.POST.get('idShop')

    return JsonResponse(SerializerComment(DB.create_comment(bodyComment, rate, idShop), many=False).data, safe=False)


# POST
def update_comment(request):
    idComment = request.POST.get('idComment')
    newRate = request.POST.get('newRate')
    newBodyOfComment = request.POST.get('newComment')

    return JsonResponse(SerializerComment(DB.update_comment(idComment, newRate, newBodyOfComment), many=False).data,
                        safe=False)



# POST
def delete_comment(request):
    idComment = request.POST.get('idComment')
    DB.delete_comment(idComment)
    return HttpResponse("Success")

