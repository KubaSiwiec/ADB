from django.contrib import admin
from .models import Seat, Movie, Room, Movie_seat, Booking
# Register your models here.
admin.site.register(Room)
admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Movie_seat)
admin.site.register(Booking)