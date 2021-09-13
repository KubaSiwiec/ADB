from django import forms
from .models import Movies, Seats, Movie_seats, Bookings
class BookSeatForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Bookings
        fields = ['seat_id']