from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         # homepage: /
    path('services/', views.services, name='services'),   # /services/
    path('portfolio/', views.portfolio, name='portfolio'), # /portfolio/
    path('gallery/', views.gallery, name='gallery'),       # /gallery/
    path('transformations/', views.transformations, name='transformations'), # /transformations/
    path('contact/', views.contact, name='contact'),       # /contact/
]
