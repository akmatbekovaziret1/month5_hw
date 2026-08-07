import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import (
    UserCreateSerializer,
    UserAuthSerializer,
    UserConfirmSerializer
)
from .models import ConfirmationCode


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    user = authenticate(**serializer.validated_data)
    if user:
        token, _ = Token.objects.get_or_create(user = user)
        return Response(data={'key': token.key})
    return Response(status = status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = User.objects.create_user(
        username = username,
        password = password,
        is_active = False
    )
    #create code (6-symbol) -> user
    #пользователь может отправить помимо username почту. Код отправляется на почту
    code = str(random.randint(100000, 999999))
    ConfirmationCode.objects.create(
        user = user,
        code = code
    )
    return Response(
        status=status.HTTP_201_CREATED,
        data={
            'user_id': user.id,
            'code': code
        }
    )
    
@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    code = serializer.validated_data.get('code')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(
            data={'error': 'User does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        confirmation = ConfirmationCode.objects.get(user=user)
    except ConfirmationCode.DoesNotExist:
        return Response(
            data={'error': 'Confirmation code does not exist'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if confirmation.code != code:
        return Response(
            data={'error': 'Invalid confirmation code'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user.is_active = True
    user.save()

    confirmation.delete()

    return Response(
        data={'message': 'User successfully confirmed'},
        status=status.HTTP_200_OK
    )