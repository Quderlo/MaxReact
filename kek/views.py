import json
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


# @csrf_exempt
# def receive_request(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode()) # Получить данные из тела запроса
#         print(data) # Вывести данные в консоль
#         return HttpResponse(status=200)
#     else:
#         return HttpResponse(status=405)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def register_user(request):
    data = json.loads(request.body.decode())
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    pass


class MyTokenVerifyView(TokenVerifyView):
    pass
