from django.urls import path
from .views import MoviesListView, MoviesDetailView
from . import views

urlpatterns = [
    path('', MoviesListView.as_view(), name='booking-home'),
    path('movie/<int:pk>', MoviesDetailView.as_view(), name='movie-detail'),
]