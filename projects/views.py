from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileDetailSerializer, ProfileSerializer

class ProfileList(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ProfileDetail(APIView):
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileDetailSerializer(profile)
        return Response(serializer.data)

# UPDATE /profile/<pk>
    def put(self, request, pk):
        profile = self.get_object(pk)
        data = request.data
        serializer = ProfileDetailSerializer(
            instance=profile,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
# DELETE /profile/<pk>
    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(dict(message= 'Profile deleted!'))