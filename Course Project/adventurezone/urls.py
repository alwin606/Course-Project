from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index_page),
    path('park/', views.park_page),
    path('restaurants/', views.restaurants_page, name="restaurants_page"),
    path('attractions/', views.attractions_page),
    path('submit_form_park/', views.submit_form_park, name='submit_form_park'),
    path('places/', views.places_page, name='places_page')
]