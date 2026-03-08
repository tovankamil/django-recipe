from rest_framework import serializers


class RoleCreateSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
