from django.urls import path, include
from django.views.generic.detail import DetailView
from api_basic.models import Snippet
from api_basic import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy',
#     'patch': 'partial_update'
# })
# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     # path("snippet-list/", views.snippet_list, name='snippet-list'),
#     path('', views.api_root),
#     path("snippets/", views.SnippetViewSet.as_view(), name='snippet-list'),
#     # path("snippet-detail/<int:pk>/", views.snippet_detail, name='snippet-detail')
#     path("snippets/<int:pk>/", views.SnippetViewSet.as_view(), name='snippet-detail'),
#     path("users/", views.UserViewSet.as_view(), name='users-list'),
#     # path("users/<int:pk>/", views.UserDetail.as_view(), name='user-detail'),
#     path("snippets/<int:pk>/highlight/", views.SnippetViewSet.as_view(), name='snippet-highlight'),
#     # path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name='snippet-highlight'),
# ]

# urlpatterns = [
#     path('', views.api_root),
#     path("snippets/", snippet_list, name='snippet-list'),
#     path("snippets/<int:pk>/", snippet_detail, name='snippet-detail'),
#     path("snippets/<int:pk>/highlight/", snippet_highlight, name='snippet-highlight'),
#     path("users/", user_list, name='users-list'),
#     path("users/<int:pk>/", user_detail, name='user-detail'),
#
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)


router = DefaultRouter()
router.register(r'api_basic', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

router1 = DefaultRouter()
router1.register(r'app-user', views.AppUserViewSet, basename='app-user')

urlpatterns = [
    path('', include(router.urls)),
    path('app-user/', include(router1.urls)),
    # path('hello/', views.UserSerializer.a),
    path('user-list/', views.ListUser.as_view()),
    path('app-user-list/', views.AppUserList.as_view()),
    # path('app-user-custom-list/', views.AppUserCustomList),
    # path('app-user-detail/<int:id>/', views.AppUserDetail.as_view()),
    # path('app-user-login/<str:username>/<str:password>/', views.AppUserViewSet.as_view({'get': 'retrieve'})),
    # path('class-view/<int:pk>/', views.SnippetDetail.as_view())
]

