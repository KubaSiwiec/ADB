from ..models import Booking, Movie, Seat, Room
def get_free_seats(movie: Movie):

    avail_list = []
    booked_already_list = []

    room = movie.room_id
    number_of_seats = room.number_of_seats
    number_of_rows = room.number_of_rows
    number_of_columns = room.number_of_columns

    avail_list =

    booking_list = Booking.objects.filter(movie_id=movie)
    for single_booking in booking_list:
        booked_already_list.append(single_booking.seat_id)