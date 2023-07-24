# serializers.py
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')

    mark_as_read = serializers.HyperlinkedIdentityField(view_name='book-mark-as-read', read_only=True,
                                                        lookup_field='pk')
    authors = serializers.HyperlinkedIdentityField(view_name='book-authors')

    class Meta:
        model = Book
        fields = ('url', 'id', 'title', 'author', 'mark_as_read', 'authors')
        # fields = '__all__'

# it will create url by default
# class BookSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('id', 'title', 'author')

        #
        # fields = '__all__'
