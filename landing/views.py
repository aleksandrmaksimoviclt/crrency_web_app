from django.shortcuts import render
from django.http import HttpResponse
from .models import Info, TeamMember, Subscriber

def index(request):
    members = TeamMember.objects.all()
    info = Info.objects.all()
    return render(request, 'landing/index.html', {'members': members, 'info': info})

def subscribe(request):
    try:
        email = request.POST.get('email', '')
        subscriber = Subscriber.objects.get(email=email)
        return HttpResponse('Already subscribed')
    except Subscriber.DoesNotExist:
        subscriber = Subscriber.objects.create(email)
        return HttpResponse('Created')
    except Subscriber.ValidationError as e:
        return HttpResponse(e)
    except Exception as e:
        return HttpResponse('Something went wrong')

