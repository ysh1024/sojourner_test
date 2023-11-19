from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import PostArgs
from .serializers import PostArgsSerializer
from rest_framework import status

from common.CommonRes import create_res

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_data(request):
    if request.method == 'GET':
        snippets = PostArgs.objects.all()
        serializer = PostArgsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostArgsSerializer(data=request.data)
        print(serializer.initial_data)
        res = create_res()

        if serializer.is_valid():
            res["result"] = serializer.initial_data

            return Response(res, status=status.HTTP_200_OK)

        else:
            res["code"] = "Error"
            res["result"] = "포맷이 적절하지 않습니다"
            return Response(res, status=status.HTTP_200_OK)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)