from django.shortcuts import render
from django.http import HttpResponse


class Views:
    @staticmethod
    def home_view(request):
        return render(request, 'home.html')
