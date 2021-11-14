from rest_framework import serializers
from.models import Profile

class ProfileSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    bio = serializers.models.CharField(max_length=250)
    first_name = serializers.models.TextField()
    photo = serializers.models.URLField()
    gender = serializers.models.TextField() 
    # experience = serializers.models.IntegerField(3)
    role = serializers.models.TextField()
    company = serializers.models.TextField() 
    facts = serializers.models.CharField(max_length=150)
    # date_created = serializers.models.DateField()
    linkedin = serializers.models.URLField()
    status = serializers.models.TextField()

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

class ProfileDetailSerializer(ProfileSerializer):
    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio',instance.bio)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.photo = validated_data.get('photo',instance.photo)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.role = validated_data.get('role',instance.role)
        instance.company = validated_data.get('company',instance.company)
        instance.facts = validated_data.get('facts',instance.facts)
        instance.linkedin = validated_data.get('linkedin',instance.linkedin)
        instance.save()
        return instance


