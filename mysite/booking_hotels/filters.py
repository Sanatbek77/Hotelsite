from django_filters import FilterSet
from.models import Hotel, Room


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city': ['exact'],
        }


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_number': ['gt', 'lt'],
            'room_type': ['exact'],
            'room_price': ['gt', 'lt'],
            'hotel_room': ['exact'],
        }
