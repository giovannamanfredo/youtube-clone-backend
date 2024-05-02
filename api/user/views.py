from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Creator
from .serializers import CreateCreatorSerializer, UpdateCreatorSerializer

class CreatorList(APIView):
    def post(self, request):
        serializer = CreateCreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreatorDetail(APIView):
    def get_object(self, username):
        try:
            return Creator.objects.get(username=username)
        except Creator.DoesNotExist:
            raise Http404

    def get(self, request, username):
        creator = self.get_object(username)
        serializer = CreateCreatorSerializer(creator)
        return Response(serializer.data)

    def put(self, request, username):
        creator = self.get_object(username)
        serializer = UpdateCreatorSerializer(creator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        creator = self.get_object(username)
        creator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)