from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flower
from .serializers import FlowerSerializer

@api_view(['GET', 'POST'])
def flower(request):

    if request.method == 'GET':
        query = Flower.objects.all()
        serializer = FlowerSerializer(query, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlowerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
