from rest_framework import serializers
from api_basic.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, AppUser
from django.contrib.auth.models import User


# class SnippetSerializer(serializers.Serializer):
#     created = serializers.DateTimeField()
#     title = serializers.CharField(default='')
#     language = serializers.CharField(default='python')
#     style = serializers.CharField(default='friendly')
#
#     def create(self, validated_data):
#         return Snippet.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'created', 'title', 'language', 'style', 'owner', 'linenos', 'code']
#
#     owner = serializers.ReadOnlyField(source='owner.username')

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
        # fields = ['id', 'username', 'password', 'set_password']


