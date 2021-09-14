This repo contains project created for purpose of Advance Databeses course.

It contains cinema seats booking system written in Django.

The project consists of two main apps:
- One (User) handles user logic with registration, login, logout, and user profile updates
- The other (Booking) handles logic connected to the booking itself

Settings are in the main ADB folder.
HTML templates are located in templates catalogue, and css in the static catalogue.

Two apps consist of files:
- models.py - creates databes tables and menagers for instance creation and querying.
- urls.py - consists of url-view-template-name mappings
- views.py - handles logic and renders templates and forms for specific urls
- forms.py - handles forms for database objects manipulation
- signals.py - only in Booking folder, handles automatic interaction between models
- and others.

Database operation:
- The only independent model is Room
- Each Movie instance has to have one foreign key of a room
- Another table is Seat - each has a name, row number, column number and room_id as foreign key
- When the new movie is created, thanks to Booking/signals.py the Movie_seats instances are created
  First the movie.room_id is taken, and then all seats id's from that room are created in Movie_seats table with movie_id pointing to movie
- Booking can be made by user, then the Bookimg instance is created, and movie_seat.busy is set to True,
  then it can't be chosen anymore by any user for the same movie
- User can modify their profile information
- User bookings can be seen as ListView
- User can delete boking while accessing it from detail view - although the form doesn't work very well, it has to be opened in the new tab for some reason
- When any object is deleted, it works as cascade and dependent records are also removed.

Systems functionality:
The application makes it possible to:
- Create, update and remove rooms, movies, seats, and any other model from admins site: http://127.0.0.1:8000/admin/ when running django server
- Register, log in, log out, udate the user profile
- Redirect to login when someone not yet logged tries to access the user information
- See map of free seats when clicking at the movie
- Book seat, redirect to profile. The seat that was booked is filtered and no loger accessible for the same movie
- User can delete their own bookings

To access admin console:
- Write in terminal from the ADB folder:
  python manage.py createsuperuser
  and choose username and password
- Go to http://127.0.0.1:8000/admin/

To get to registration page and then log in:
- Run server with python manage.py runserver
- Go to http://127.0.0.1:8000/register/
- After registration log in when redirected to login page

File 'Select movie_seat to change _ Django site admin - Google Chrome 2021-09-15 00-20-19.mp4' has a video of using application, it could be helpful, but I can't record soung on my PC for some reason 
