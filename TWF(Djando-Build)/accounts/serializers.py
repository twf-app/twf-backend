from django.contrib.auth.models import Group
from rest_framework import serializers

from accounts.models import Member


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('username', 'phone', 'email', 'image', 'default_location',)
