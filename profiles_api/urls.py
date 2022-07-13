
from profiles_api import views
from django.conf.urls import url


urlpatterns = [
    url('hello-view/', views.HelloAPIView.as_view()),
]
