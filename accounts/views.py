from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user

class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            print(user)

            send_code_to_user(user['email'])
            return Response({
                'data': user,
                'message': f"Hi {user['first_name']} thanks for signing up"
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
