from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView
from Booking.models import Booking
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # zapisuje formę
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can no log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)

# def movie_list_view(request):
#     if request.user.is_authenticated:
#         username = request.user.username
#         user = User.objects.get(username=username)
#     users_movies = Booking.objects.filter(user_id=user).values('movie_id')
#     users_seats = Booking.objects.filter(user_id=user).values('seat_id')
#     book_dict = {}
#     for i, movie in enumerate(users_movies):
#         book_dict[movie] = users_seats[i]
#     context = {
#         'user_books': book_dict
#     }
#     return render(request, 'user/user_bookings.html', context)


class BookingsListView(ListView):
    model = Booking
    template_name = 'Users/user_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        bookings = Booking.objects.filter(user_id=self.request.user)
        return bookings

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'Users/booking.html'

class DeleteMe(DeleteView):
    template_name = 'deleteconfirmation.html'
    model = Booking
    success_url = '/user_bookings'

