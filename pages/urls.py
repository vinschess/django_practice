from django.urls import path

# from pages.views import AboutPageView
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('about/', AboutPageView.as_view(), name='about'),
]