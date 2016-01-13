from django.shortcuts import render
from django.http import HttpResponse
from .models import Info, TeamMember, Subscriber
from django.views.decorators.csrf import csrf_exempt 


def index(request):
    members = TeamMember.objects.all()
    info = Info.objects.all()
    return render(request, 'landing/index.html', {'members': members, 'info': info})

@csrf_exempt
def subscribe(request):
    try:
        email = request.POST.get('email', '')
        subscriber = Subscriber.objects.get(email=email)
        return HttpResponse('Already subscribed')

    except Subscriber.DoesNotExist:
        subscriber = Subscriber.objects.create(email=email)
        return HttpResponse('Created')

    except Subscriber.ValidationError as e:
        return HttpResponse(e)
        
    except Exception as e:
        return HttpResponse('Something went wrong')

