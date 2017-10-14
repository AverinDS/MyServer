from ..models.Comment import Comment
from ..models.Product import Product
from ..models.Shop import Shop


def select_all_Shop():
    return Shop.objects.all()


def select_products_from_shop(shopId):
    return Product.objects.filter(shopFK=shopId)


def get_comments_about_shop(shopId):
    return Comment.objects.filter(shopFK=shopId)
