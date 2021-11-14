from rest_framework import serializers
from.models import Profile

class ProfileSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    bio = serializers.models.CharField(max_length=250)
    first_name = serializers.models.TextField()
    photo = serializers.models.URLField()
    gender = serializers.models.TextField() 
    experience = serializers.models.IntegerField()
    role = serializers.models.TextField()
    company = serializers.models.TextField() 
    facts = serializers.models.CharField(max_length=150)
    date_created = serializers.models.DateField()
    linkedin = serializers.models.URLField()
    status = serializers.models.TextField()

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)