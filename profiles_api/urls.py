
from profiles_api import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    url('hello-view/', views.HelloAPIView.as_view()),
    url('login/', views.UserLoginAPIView.as_view()),
    url('', include(router.urls))

]
