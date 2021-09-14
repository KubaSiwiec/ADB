from Booking import models


def get_free_seats(movie: models.Movie):
    bookings = models.Booking.objects.filter(movie_id=movie)
    movie_seats = models.Movie_seat.objects.filter(movie_id=movie)
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


def print_seats(movie_title: str):
    movie = models.Movie.objects.get(title=movie_title)
    room_id = movie.room_id
    room = models.Room.objects.get(name=room_id)
    num_rows = room.number_of_rows
    num_cols = room.number_of_columns

    room_seats_string = '<h4>Seats map:</h4>\n<table class="fixed" border="1"><thead><tr>'
    for column_int in range(room.number_of_columns + 1):
        room_seats_string += '<col width = "30px"/>'
    room_seats_string += '<th>Row\Col</th>'
    for column_int in range(room.number_of_columns):
        room_seats_string += '<th>' + chr(column_int + 65) + '</th>'
    room_seats_string += '</tr></thead><tbody>'
    free_seats = get_free_seats(movie)
    free_seats_names = []
    for free_seat in free_seats:
        free_seats_names.append(free_seat.name)
    # print(free_seats)

    for row in range(1, room.number_of_rows + 1):
        room_seats_string += '<tr height="30px"><td>'+ str(row) + '</td>'
        for column_int in range(room.number_of_columns):
            column = chr(column_int + 65)
            seat_name = room.name[-1] + '_' + column + str(row)
            # print(seat_name)
            if seat_name in free_seats_names:
                room_seats_string += '<td bgcolor="green"></td>'
            else:
                room_seats_string += '<td bgcolor="red">X</td>'
        room_seats_string += '</tr>'
    room_seats_string += '</tbody></table>'
    print(room_seats_string)
    return room_seats_string
