from django.urls import path
from . import views
urlpatterns = [
    path('stripePayment/', views.post, name='stripePayment'),
]