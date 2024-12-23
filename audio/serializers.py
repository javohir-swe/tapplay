from rest_framework import serializers

from .models import Audio



class AudioListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = "__all__"