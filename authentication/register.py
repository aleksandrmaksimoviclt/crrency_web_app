from django.core.mail import EmailMessage
from django.contrib.auth.models import User


def check_existing(username, email):
    try:
        User.objects.get(username=username)
        User.objects.get(email=email)
        exist = True
    except User.DoesNotExist:
        exist = False
    except Exception:
        exist = True
    return exist

def register(request):
    try:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        exist = check_existing(username, email)
        if not exist:
            user = User.objects.create_user(username, email, password, is_active=False)
            state, msg = activation_mail(user)
            return True, 'User successfully created'
    except Exception as e:
        print(e)
        return False, e
    return False, 'User already exists'

def activation_mail(user):
    try:
        hyperlink = 'http://127.0.0.1/authentication/user/%s/activate' % user.id
        email = EmailMessage('Crrency.co', 'Hi %s, Your account have been successfully created.' \
            'You can access our website by pressing this link ' \
            '%s' % (user.username, hyperlink), to=[user.email])
        email.send()
        return True, 'successfully sent'
    except Exception as e:
        print(e)
        return False, e

def user_activate(id):
    try:
        user = User.objects.get(id=id)
        if user.is_active == False:
            user.is_active = True
            user.save()
            msg = 'Succesfully activated'
        else:
            msg = 'User is already active'
    except Exception as e:
        msg = e
    return msg