from rest_framework import serializers
from .models import *

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  'created_date',]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name',]


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CitySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name',]


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name',]


class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_images',]


class HotelListSerializers(serializers.ModelSerializer):
    city = CitySimpleSerializers()
    country = CountrySerializers()
    owner = UserProfileSimpleSerializers()
    hotels_image = HotelImageSerializers(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id','hotel_name','country',
                  'city','address','owner','hotels_image']


class HotelSimpleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ['hotel_name',]


class HotelDetailSerializers(serializers.ModelSerializer):
    city = CitySimpleSerializers()
    country = CountrySerializers()
    owner = UserProfileSimpleSerializers()
    hotels_image = HotelImageSerializers(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name','owner','country','city',
                  'address','hotel_video','hotel_stars','created_date', 'hotels_image']


class RoomListSerializers(serializers.ModelSerializer):
    hotel_room = HotelSimpleSerializers()
    room_images = RoomImageSerializers(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id','room_price','hotel_room',
                  'room_type', 'room_status','room_description', 'room_images']


class RoomDetailSerializers(serializers.ModelSerializer):
    room_images = RoomImageSerializers(many=True, read_only=True)

    class Meta:
        model = Room

        fields = ['id','room_number','hotel_room','room_type','room_status',
                  'room_price','all_inclusive',
                  'room_description', 'room_images']


class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','user_name','hotel','text','stars','parent',]


class ReviewDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

