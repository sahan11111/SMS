from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import *
from rest_framework.mixins import CreateModelMixin
from .models import User
from .serializers import *


# Create your views here.
class UserViewSet(GenericViewSet,CreateModelMixin):
    queryset=User.objects.all()
    serializer_class=Userseralizer
    