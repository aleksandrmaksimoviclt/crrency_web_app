from django.shortcuts import render
from django.http import HttpResponse
from .models import Info, TeamMember

def index(request):
    members = TeamMember.objects.all()
    info = Info.objects.all()
    return render(request, 'landing/index.html', {'members': members, 'info': info})