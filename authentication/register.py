from django.core.mail import EmailMessage
from django.contrib.auth.models import User


hyperlink_format = '<a href="{link}">{text}</a>'
hyperlink = hyperlink_format.format(link='https://frozen-hamlet-3237.herokuapp.com/', text='Crrency')

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
        import pdb; pdb.set_trace()
        if not exist:
            user = User.objects.create_user(username, email, password, is_active=False)
            activation_mail(user)
            return True, 'User successfully created'
    except Exception as e:
        print(e)
        return False, e
    return False, 'User already exists'

def activation_mail(user):
    hyperlink += '/authentication/user/%s/activate' % user.id
    email = EmailMessage('Crrency.co', 'Hi %s, You have successfully created.' \
        'You can access our website by pressing this link' \
        '%s' % (user.username, hyperlink), [user.email])
    email.send()