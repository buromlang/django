from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet, AppUser
from .serializers import SnippetSerializer, UserSerializer,AppUserSerializer
from rest_framework.decorators import api_view, APIView, action, throttle_classes, schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics, permissions, authentication
from django.contrib.auth.models import User
from api_basic.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle
from rest_framework.schemas import AutoSchema
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


# @csrf_exempt
# def snippet_list(request):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=400)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)


# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# class SnippetList(APIView):
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         try:
#            return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# #
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['get'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'api_basic': reverse('snippet-list', request=request, format=format)
    })


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

class CustomPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'pag'
    page_size_query_param = 'page_size_query'
    max_page_size = 5
    last_page_strings = 'last'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    template = 'rest_framework/pagination/previous_and_next.html'
    limit_query_param = 'limit_query'
    offset_query_param = 'offset_query'
    max_limit = 3


class CustomCursorPagination(CursorPagination):
    page_size = 3


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    pagination_class = CustomCursorPagination
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

# class CustomAutoSchema(AutoSchema):
#     def get_link(self, path, method, base_url):
#         return vie


@api_view(['get', 'post'])
@throttle_classes([OncePerDayUserThrottle])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "post", "data": request.data})
    return Response({"messagesss": "hello world"})


@throttle_classes([OncePerDayUserThrottle])
class ListUser(APIView):
    queryset = User.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = UserSerializer

    def get(self, request):
        users = [user.username for user in User.objects.all()]
        return Response(users)


class AppUserList(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(username='burom1')
        serializer = AppUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        queryset = AppUser.objects.filter(username=self.request.data['username'])
        if queryset.exists():
            raise ValidationError('You have already signed up')
        serializer.save(username=self.request.data.username)


class AppUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'id'


class AppUserViewSet(viewsets.ModelViewSet):
    """ It checks AppUser Login credentials verification """
    queryset = AppUser.objects.all()
    lookup_field = 'username'
    serializer_class = AppUserSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        queryset = get_object_or_404(self.queryset, username=kwargs['username'])
        if queryset.password == kwargs['password']:
            return Response("logged in")
        return Response("Failed")


# need to check below code
# class CustomFilterMixin:
#     queryset = AppUser.objects.all()
#
#     def get_object(self):
#         queryset = self.get_queryset().filter(username='burom')
#         return queryset
#
#
# class AppUserCustomList(generics.CreateAPIView, CustomFilterMixin):
#     queryset = AppUser.objects.all()
#     serializer_class = AppUserSerializer
#
#     def get(self, request, format=None):
#         queryset = self.get_object()
#         serializer = AppUserSerializer(queryset, many=True)
#         return Response(serializer.data)

# END

