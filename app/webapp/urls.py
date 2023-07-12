from django.urls import path

from webapp.views.home import *

urlpatterns = [
    path('', homeView.as_view(), name='home'),
]