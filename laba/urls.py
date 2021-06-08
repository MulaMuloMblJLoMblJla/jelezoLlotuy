from django.urls import path

from .views import FormView, ReviewsView, ListView, TableView, ContactView, MyRegistration
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', FormView.as_view(), name='form'),
    path('add-review/', ReviewsView.as_view(), name='review'),
    path('list/', ListView.as_view(), name='list'),
    path('table/', TableView.as_view(), name='table'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', MyRegistration.as_view(), name='register'),
]
