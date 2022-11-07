"""app views module"""

from django.shortcuts import render


def home_view(request):
    """Home View"""
    return render(request, 'templates/app/index.html')
