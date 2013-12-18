from django.shortcuts import render
from app.models import Articles


def index(request):
    articles = Articles.objects.all()
    return render(request, 'app/index.html', {'articles': articles})