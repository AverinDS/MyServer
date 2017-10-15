from ..models.Comment import Comment
from ..models.Product import Product
from ..models.Shop import Shop


def select_all_Shop():
    return Shop.objects.all()


def select_products_from_shop(shopId):
    return Product.objects.filter(shopFK=shopId)


def get_comments_about_shop(shopId):
    return Comment.objects.filter(shopFK=shopId)


def create_comment(commentOfUser, rateUser, idShop):
    comment = Comment(rate=rateUser, bodyOfLine=commentOfUser, shopFK=idShop)
    comment.save()
    return Comment.objects.filter(rate=rateUser, bodyOfLine=commentOfUser, shopFK=idShop)


def update_comment(idComment, newRate, newComment):
    comment = Comment.objects.filter(id=idComment)
    comment.rate = newRate
    comment.commentLine = newComment
    comment.save()
    return Comment.objects.filter(id=idComment)


def delete_comment(idComment):
    comment = Comment.objects.filter(id=idComment)
    comment.delete()


