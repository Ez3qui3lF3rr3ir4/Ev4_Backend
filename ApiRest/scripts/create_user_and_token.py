import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ApiRest.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()
username = 'apitest'
email = 'apitest@example.com'
password = 'testpass'

user, created = User.objects.get_or_create(username=username, defaults={'email': email})
if created:
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print('created')
else:
    print('exists')

token, _ = Token.objects.get_or_create(user=user)
print('token:', token.key)
