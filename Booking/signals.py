from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie, Seat, Movie_seat


@receiver(post_save, sender=Movie)
def create_movie_seats(sender, instance, created, **kwargs):
    if created:
        room = instance.room_id
        seats = Seat.objects.filter(room_id=room)
        for seat in seats:
            movie_seat = Movie_seat.objects.create(seat_id=seat, movie_id=instance)
            movie_seat.save()
