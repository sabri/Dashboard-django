from .models import *
from rest_framework import serializers ####### serializers: qui faire la liaison
from django.contrib.auth.models import User

class jsonFis(serializers.ModelSerializer):
    class Meta:
        model=Desktop
        fields='__all__'######## tous le table au lieu d'ecrire le code json faire __all__

class jsonFis2(serializers.ModelSerializer):
    class Meta:
        model=Laptop
        fields='__all__'


class json_user(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


