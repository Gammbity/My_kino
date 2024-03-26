from django.shortcuts import render
from .models import CommentModel, FilmModel, AktyorModel, User
from .serializers import CommentSerializer, FilmSerializer, AktyorSerializer, AddActorSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers

class FilmApiView(APIView):
    
    def get(self, request):
        film = FilmModel.objects.all()
        serializer = FilmSerializer(film, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=FilmSerializer)
    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=FilmSerializer)
    def put(self, request, pk):
        film = FilmModel.objects.get(pk=pk)
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=FilmSerializer)
    def patch(self, request, pk):
        film = FilmModel.objects.get(pk=pk)
        serializer = FilmSerializer(film, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            film = FilmModel.objects.get(pk=pk)
            film.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'error', 'message': f"{e}"})
        
class AktyorApiView(APIView):

    def get(self, request):
        aktyors = AktyorModel.objects.all()
        serializer = AktyorSerializer(aktyors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=AktyorSerializer)
    def post(self, request):
        serializer = AktyorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=AktyorSerializer)
    def put(self, request, pk):
        aktyor = AktyorModel.objects.get(pk=pk)
        serializer = AktyorSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        aktyor = AktyorModel.objects.get(pk=pk)
        serializer = AktyorSerializer(aktyor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            aktyor = AktyorModel.objects.get(pk=pk)
            aktyor.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'error', 'message': f"{e}"})
        
class CommentApiView(APIView):
    def get(self, request):
        comment = CommentModel.objects.filter(user=request.user.id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddAktyorViewSet(ModelViewSet):
    queryset = FilmModel.objects.all()
    serializer_class = AddActorSerializer

    @action(methods=['post'], detail=True)
    def add_aktyor(self, request, pk=None):
        actor = request.data['actor']
        actors = AktyorModel.objects.all()
        film = FilmModel.objects.get(pk=pk)
        if actor in actors:
            film.actors.add(actor)
            film_serializer = AddActorSerializer(film, many=True)
            return Response(film_serializer.data)
        e = f"{actor} ushbu ID dagi aktyor hali mavjud emas!"
        raise serializers.ValidationError({'aktyor': e})