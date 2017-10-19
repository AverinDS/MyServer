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
    comment = Comment(rate=rateUser, commentLine=commentOfUser, shopFK=Shop.objects.get(id=idShop))
    comment.save()
    return Comment.objects.filter(rate=rateUser, commentLine=commentOfUser, shopFK=Shop.objects.get(id=idShop)).last().id

def update_comment(idComment, newRate, newComment):
    comment = Comment.objects.get(id=idComment)
    comment.rate = newRate
    comment.commentLine = newComment
    comment.save()
    return True


def delete_comment(idComment):
    comment = Comment.objects.get(id=idComment)
    comment.delete()
    return True
