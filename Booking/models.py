from django.db import models
from django.contrib.auth import get_user_model
# from .booking_functions.availability import get_free_seats

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()
    number_of_rows = models.IntegerField()
    number_of_columns = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    director = models.CharField(max_length=100)
    scriptwriter = models.CharField(max_length=100)
    studio = models.CharField(max_length=100)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Seat(models.Model):
    name = models.CharField(max_length=4, default="A_1A")
    row = models.IntegerField()
    column = models.CharField(max_length=1)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Movie_seat(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    busy = models.BooleanField(default=False)
    def __str__(self):
        return str(self.seat_id.name)


class Booking(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seat_id.name) + ', ' + str(self.user_id.username) + ', ' + str(self.movie_id.title)