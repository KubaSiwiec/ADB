from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView
from Booking.models import Booking
from django.contrib.auth.mixins import LoginRequiredMixin

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


class BookingsListView(ListView, LoginRequiredMixin):
    model = Booking
    template_name = 'Users/user_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        bookings = Booking.objects.filter(user_id=self.request.user)
        return bookings


class BookingDetailView(DetailView, LoginRequiredMixin):
    model = Booking
    template_name = 'Users/booking.html'


class DeleteMe(DeleteView, LoginRequiredMixin):
    template_name = 'deleteconfirmation.html'
    model = Booking
    success_url = '/user_bookings'

