from django.urls import path
from managers import views

#urlpatterns=[
 #   path("index",views.index),
  #  path("login",views.login)
#]


urlpatterns=[
    path("index",views.IndexView.as_view()),
    path("login",views.LoginView.as_view()),
    path("reg",views.RegView.as_view()),
]