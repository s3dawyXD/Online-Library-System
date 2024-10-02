from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from users.models import User
from users.api.serializers import (
    UserSerializer,
    UserRegistrationSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[],
        serializer_class=UserRegistrationSerializer,
    )
    def registration(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = serializer.save()
        return Response(UserSerializer(new_user).data, status=status.HTTP_201_CREATED)
