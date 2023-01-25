from rest_framework.generics import get_object_or_404
from django.template import context
from .serializers import bikeSerializer
# from rest_framework.exceptions import NotFound
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response 
from .models import Bike
from rest_framework.permissions import (AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)

class BikeView(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = bikeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    
    def getAllBikes(self,request):
        serializer = bikeSerializer.getAllBikes(context)
        return Response(serializer,status=status.HTTP_200_OK)

    def createBike(self, request):

        serializer_context = {
            'number': request.data['number'],
            'warning': request.data['warning'],
            'disabled': request.data['disabled'],
            'request': request
        }

        serializer_data = request.data

        serializer = self.serializer_class(
            data = serializer_data,
            context = serializer_context
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


    def updateBike(self, request, number):
        bike = get_object_or_404(Bike.objects.all(), number=number)
        data = request.data
                
        serializer = bikeSerializer(
            instance=bike, data=data, partial=True)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
        return Response(serializer.data)

    def deleteBike(self, request, number):
        bike = get_object_or_404(Bike.objects.all(), number=number)
        bike.delete()
        return Response({'data': 'Bike deleted'})
