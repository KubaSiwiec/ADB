from django.urls import path
from .views import MoviesListView, MoviesDetailView, movie_detail_view
from . import views

urlpatterns = [
    path('', MoviesListView.as_view(), name='booking-home'),
    path('movie/<int:primary_key>', movie_detail_view, name='movie-detail'),
]