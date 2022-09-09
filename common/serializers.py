from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from common.models import Task


class TaskSerializer(serializers.Serializer):
    desc = serializers.CharField()
    status = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.desc = validated_data.get('desc', instance.desc)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
