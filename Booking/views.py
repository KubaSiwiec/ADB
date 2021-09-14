from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Movie
from .forms import BookSeatForm
from .booking_functions.availability import get_free_seats

# Create your views here.
def home(request):
    context = {
        'movies': Movies.objects.all()
    }
    return render(request, 'Booking/home.html', context)

# lists all movies
class MoviesListView(ListView):
    model = Movie
    template_name = 'Booking/home.html'
    context_object_name = 'movies'
    ordering = ['date']

class MoviesDetailView(DetailView, FormMixin):
    model = Movie
    template_name = 'Booking/movie-detail.html'
    form_class = BookSeatForm

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(MoviesDetailView, self).get_context_data(**kwargs)
        context['b_form'] = BookSeatForm(initial={'seat_id': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(MoviesDetailView, self).form_valid(form)