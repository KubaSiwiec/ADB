from django.shortcuts import render
from django.views.generic import ListView
from .models import Movies

# Create your views here.
def home(request):
    context = {}
    return render(request, 'Booking/home.html', context)

# lists all movies
class PostListView(ListView):
    model = Movies