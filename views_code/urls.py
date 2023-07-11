from django.urls import path
from views_code import views
from views_code.views import MyView, HomePageView, RedirectMethod, ArticleDetailView, ArticleListView, \
    ContactFormView, ManufacturerCreateView, ManufacturerDetailView, ManufacturerUpdateView, ManufacturerDeleteView, \
    ManufactureListView, ArticleYearArchiveView, ArticleMonthArchiveView, ArticleWeekArchiveView, \
    ArticleDayArchiveView
from django.views.generic.base import RedirectView
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView, DateDetailView
from views_code.models import Article

urlpatterns = [
    path("", views.current_datetime, name="current_datetime"),
    path("<int:question_id>/", views.question_detail, name="question_detail"),
    # path("get_form", views.get_form, name="get_form"),
    path("my_view/", MyView.as_view(), name="my_view"),
    path("home_page/", HomePageView.as_view(), name="home_page"),
    path("redirect_url/<int:pk>/", RedirectMethod.as_view(), name="redirect_url"),
    path("details/<int:pk>/", HomePageView.as_view(), name="question-detail"),
    path("go-to-django/", RedirectView.as_view(url="https://www.djangoproject.com/"), name="go-to-django"),
    path("detail-view/<slug:slug>/", ArticleDetailView.as_view(), name="article-detail"),
    # path("detail-view/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("list_view/", ArticleListView.as_view(), name='article_list'),
    path("form-view/", ContactFormView.as_view(), name="form-view"),
    path("create-view/", ManufacturerCreateView.as_view(), name="create_view"),
    path("manufacturer-detail/<int:pk>", ManufacturerDetailView.as_view(), name="manufacturer-detail"),
    path("manufacturer-update/<int:pk>", ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturer-delete/<int:pk>", ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
    path("manufacturer-list/", ManufactureListView.as_view(), name="manufacturer-list"),
    path("archive/", ArchiveIndexView.as_view(model=Article, date_field='pub_date', allow_future=True),
         name="article-archive"),
    path("article-year/<int:year>/", ArticleYearArchiveView.as_view(), name="article-year-archive"),
    path("<int:year>/<int:month>/", ArticleMonthArchiveView.as_view(month_format="%m"), name="article-month-numeric"),
    path("<int:year>/<str:month>/", ArticleMonthArchiveView.as_view(), name="archive-month"),
    path("<int:year>/week/<int:week>/", ArticleWeekArchiveView.as_view(), name="archive-week"),
    path("<int:year>/<str:month>/<int:day>/", ArticleDayArchiveView.as_view(), name="archive-day"),
    # path("today/", ArticleTodayArchiveView.as_view(), name="archive-today"),
    path("today/", TodayArchiveView.as_view(model=Article, date_field='pub_date'), name="archive-today"),
    path("<int:year>/<str:month>/<int:day>/<int:pk>/", DateDetailView.as_view(model=Article, date_field='pub_date'),
         name="archive-date-detail"),

]
