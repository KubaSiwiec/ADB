from django.shortcuts import render
from django.views.generic import ListView
from .models import Movies

# Create your views here.
def home(request):
    context = {
        'movies': Movies.objects.all()
    }
    return render(request, 'Booking/home.html', context)

# lists all movies
class PostListView(ListView):
    model = Movies
    template_name = 'Booking/home.html'
    context_object_name = 'movies'
    ordering = ['date', 'time']