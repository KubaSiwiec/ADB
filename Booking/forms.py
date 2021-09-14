from django import forms
from django.core.validators import RegexValidator
from .models import Movie, Seat, Movie_seat, Booking

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class BookSeatForm(forms.Form):
    seat_column = forms.CharField(max_length=1, required=True, validators=[alphanumeric])
    seat_row = forms.IntegerField(max_value=15, required=True)
