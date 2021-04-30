from django.urls import path
from .views import AboutPageView, HomePageView, homePageView

urlpatterns = [
    #path('', homePageView, name='home_first'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
