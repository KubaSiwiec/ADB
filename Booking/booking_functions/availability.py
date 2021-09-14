from ..models import Booking, Movie, Movie_seat, Seat, Room
def get_free_seats(movie: Movie):
    bookings = Booking.objects.filter(movie_id=movie)
    movie_seats = Movie_seat.objects.filter(movie_id = movie)
    # nie działąją list comprehension, sprawdź później
    # booked_seats = [booking.seat_id for booking in bookings]
    # free_seats = [movie_seat.seat_id for movie_seat in movie_seats if movie_seat.seat_id not in booked_seats]

    booked_seats = []
    free_seats = []
    for booking in bookings:
        booked_seats.append(booking.seat_id)
    for movie_seat in movie_seats:
        if movie_seat.seat_id not in booked_seats:
            free_seats.append(movie_seat.seat_id)
    return free_seats