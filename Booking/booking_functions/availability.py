from ..models import Booking, Movie, Movie_seat, Seat, Room


def get_free_seats(movie: Movie):
    bookings = Booking.objects.filter(movie_id=movie)
    movie_seats = Movie_seat.objects.filter(movie_id=movie)
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


def print_seats(movie: Movie):
    movie = Movie.objects.get(title=movie)
    room_id = movie.room_id
    room = Room.objects.get(name=room_id)
    num_rows = room.number_of_rows
    num_cols = room.number_of_columns

    room_seats_string = ' '
    for column_int in range(room.number_of_columns):
        room_seats_string += ' ' + chr(column_int + 65) + ' '
    room_seats_string += '\n' + '_' * num_cols * 3  + '\n'
    free_seats = get_free_seats(movie)
    free_seats_names = []
    for free_seat in free_seats:
        free_seats_names.append(free_seat.name)
    # print(free_seats)

    for row in range(1, room.number_of_rows + 1):
        room_seats_string += str(row)
        for column_int in range(room.number_of_columns):
            column = chr(column_int + 65)
            seat_name = room.name[-1] + '_' + column + str(row)
            # print(seat_name)
            if seat_name in free_seats_names:
                room_seats_string += '| |'
            else:
                room_seats_string += '|X|'
        room_seats_string += '\n'
    room_seats_string += '_' * num_cols * 3
    return room_seats_string
