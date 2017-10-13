from django.http import HttpResponse, JsonResponse
from .models import Shop, Product, Comment
from .serializers import ServerSealizerShop, ServerSealizerProduct, ServerSealizerComment


def index(request):
    return HttpResponse("Congratulations! It is index page!")


def select_all(request):
    shops = Shop.objects.all()
    serializer = ServerSealizerShop(shops, many=True)
    return JsonResponse(serializer.data, safe=False)


def select_shop_town(request, town):
    shops = ""


def select_product_from_shop(request, shopId):
    products = Product.objects.filter(shopFK=shopId)
    serializer = ServerSealizerProduct(products, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_comments_to_shop(request, shopId):
    comments = Comment.objects.filter(shopFK=shopId)
    serializer = ServerSealizerComment(comments, many=True)
    return JsonResponse(serializer.data, safe=False)


def update_comment(request, shopId, newLine):
    c = ""


def delete_comment(request, shopId, line ):
    c = ""


def create_comment(request, shopId, line, rate_user):
    comment = Comment(rate=rate_user, commentLine=line, shopFK=shopId)
    try:
        comment.save()
        return HttpResponse("success", status=200)
    except():
        return HttpResponse("fail", status=500)


