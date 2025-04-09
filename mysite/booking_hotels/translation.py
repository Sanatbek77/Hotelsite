from .models import City, Hotel, Room, Review, Country
from modeltranslation.translator import TranslationOptions,register

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_description', 'country',)


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_description',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('user_name','hotel', 'text', )




