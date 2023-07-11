from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_name/", views.get_name, name="get_name"),
    path("thankyou/", views.get_name, name="thankyou"),
    path("to_send_mail/", views.to_send_mail, name="to_send_mail"),
    path("student_detail/", views.student_detail, name="student_detail"),
    ]
