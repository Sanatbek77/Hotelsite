from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'cities', CityViewSet, basename='city_list'),
router.register(r'countries', CountryViewSet, basename='country_list'),


urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register_list'),
    # path('login/', CustomLoginView.as_view(), name='login_list'),
    # path('logout/', LogoutView.as_view(), name='logout_list'),

    path('', include(router.urls)),
    path('hotels/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/',  HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/',  RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/',  RoomDetailAPIView.as_view(), name='room_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileEditAPIView.as_view(), name='user_detail'),
    path('reviews/', ReviewListAPIView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review_detail'),

]