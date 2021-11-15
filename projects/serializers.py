from rest_framework import serializers
from.models import Profile, experience_choices

class ProfileSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    bio = serializers.CharField(max_length=250)
    first_name = serializers.CharField()
    photo = serializers.URLField()
    gender = serializers.CharField() 
    experience = serializers.ChoiceField(choices=experience_choices)
    role = serializers.CharField()
    company = serializers.CharField() 
    facts = serializers.CharField(max_length=150)
    linkedin = serializers.URLField()
    status = serializers.CharField()
    date_created = serializers.DateTimeField()

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

class ProfileDetailSerializer(ProfileSerializer):
    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio',instance.bio)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.photo = validated_data.get('photo',instance.photo)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.experience = validated_data.get('experience',instance.experience)
        instance.role = validated_data.get('role',instance.role)
        instance.company = validated_data.get('company',instance.company)
        instance.facts = validated_data.get('facts',instance.facts)
        instance.linkedin = validated_data.get('linkedin',instance.linkedin)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.save()
        return instance


