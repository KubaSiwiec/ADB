from django import forms
from .models import Movie, Seat, Movie_seat, Booking


class BookSeatForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Booking
        fields = ['seat_id']

class SeatForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Seat
        fields = ['row', 'column']

