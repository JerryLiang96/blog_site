from rest_framework import serializers
from .models import Nav


class NavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ('name',)
