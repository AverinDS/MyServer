from django.db import models
from .Shop import Shop


class Comment(models.Model):
    rate = models.IntegerField(default=0)
    commentLine = models.TextField(default="")
    shopFK = models.ForeignKey(Shop)

    def __str__(self):
        return self.commentLine

    class Meta:
        db_table = "comment"
