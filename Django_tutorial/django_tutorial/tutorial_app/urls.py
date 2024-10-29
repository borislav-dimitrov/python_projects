from django.urls import path
from tutorial_app.views import Views

urlpatterns = [
    path('', Views.home_view, name='home'),
]
