from ..models import Seat, Room

def create_seats():
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    nums = [1,2,3,4,5,6,7,8]

    for letter in letters:
        for num in nums:
            for room_name in Room.objects.all():
                seat_name = room_name.name[-1] + '_' + letter + str(num)
                room = Room.objects.get(name=room_name)
                seat = Seat.objects.create(name = seat_name, row = num, column = letter, room_id = room)
                seat.save()
