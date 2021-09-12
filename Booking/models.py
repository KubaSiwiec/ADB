from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()
    number_of_rows = models.IntegerField()
    number_of_columns = models.CharField(max_length=1)

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    director = models.CharField(max_length=100)
    scriptwriter = models.CharField(max_length=100)
    studio = models.CharField(max_length=100)
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Seats(models.Model):
    row = models.IntegerField()
    column = models.CharField(max_length=1)
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)


class Bookings(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seats, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)