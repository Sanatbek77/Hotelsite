from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    ROLE_CHOICES =(
        ('client', 'client'),
        ('owner', 'owner'),
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='client'),
    phone_number = PhoneNumberField(null=True, blank=True)
    country_user = models.CharField(max_length=32,)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(70)], null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class City(models.Model):
    city_image = models.ImageField(upload_to='city_images')
    city_name = models.CharField(max_length=32)

    def __str__(self):
        return self.city_name


class Country(models.Model):
    country_name = models.CharField(max_length=32)

    def __str__(self):
        return self.country_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=32)
    hotel_stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    hotel_video = models.FileField(upload_to='hotel_video/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.hotel_name}, {self.country}, {self.city}'

    def get_average_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings)/ratings.count(),1)
        return 0


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotels_image')
    hotel_images = models.ImageField(upload_to='hotel_image/')

    def __str__(self):
        return f'{self.hotel_images}'


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    hotel_room = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('люкс','люкс'),
        ('семейный','семейный'),
        ('oдноместный','oдноместный'),
        ('двухместный','двухместный')
    )

    room_type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    STATUS_CHOICES = (
        ('свободен', 'свободен'),
        ('забронирован', 'забронирован'),
        ('занят', 'занят'),
    )
    room_status = models.CharField(max_length=16,choices=STATUS_CHOICES,default='свободен')
    room_price = models.PositiveSmallIntegerField()
    all_inclusive = models.BooleanField(default=False)
    room_description = models.TextField()

    def __str__(self):
        return f'{self.hotel_room}, {self.room_number}, {self.room_type}'


class RoomImage(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE, related_name='room_images')
    room_image = models.ImageField(upload_to='room_image/', )
    def __str__(self):
        return f'{self.room}'


class Review(models.Model):
    user_name = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    stars = models.IntegerField(choices=[(i, str(i))for i in range(1,11)],null=True,blank=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.user_name}, {self.hotel},'


class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    STATUS_BOOK_CHOICES = (
        ('отменено', 'отменено'),
        ('подтверждено', 'подтверждено')
    )
    status_book = models.CharField(max_length=16, choices=STATUS_BOOK_CHOICES)

    def __str__(self):
        return f'{self.user_book}, {self.hotel_book},'


