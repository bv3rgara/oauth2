from rest_framework import serializers

class ResourceSerializer(serializers.Serializer):
    data = serializers.CharField()
