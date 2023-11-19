from rest_framework import serializers
from .models import PostArgs

class PostArgsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostArgs
        fields = '__all__'