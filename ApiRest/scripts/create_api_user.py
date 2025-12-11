import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ApiRest.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'apitest'
email = 'apitest@example.com'
password = 'testpass'
if User.objects.filter(username=username).exists():
    print('exists')
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print('created')
