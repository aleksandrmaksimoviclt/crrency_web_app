from django.core.mail import EmailMessage
from django.contrib.auth.models import User


hyperlink_format = '<a href="{link}">{text}</a>'
hyperlink = hyperlink_format.format(link='https://frozen-hamlet-3237.herokuapp.com/dashboard', text='Crrency')

def check_existing(username, email):
    try:
        User.objects.get(username=username)
        User.objects.get(email=email)
        exist = True
    except DoesNotExist:
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
            User.objects.create_user(username, email, password,) #is_active=False)
            activate(username, email)
            return True, 'User successfully created'
    except Exception as e:
        return False, e
    return False, 'User already exists'

def activate(username, email):
    email = EmailMessage('Crrency', 'Hi %s, You have successfully created. You can access our website by pressing this link %s' % (username, hyperlink), [email])
    email.send()