from django.contrib import admin
from .models import Seat, Movie, Room
# Register your models here.
admin.site.register(Room)
admin.site.register(Movie)
admin.site.register(Seat)