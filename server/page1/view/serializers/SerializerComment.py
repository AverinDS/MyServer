from rest_framework import serializers
from ..work_with_DB import Comment


class SerializerComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'rate', 'commentLine', 'shopFK')