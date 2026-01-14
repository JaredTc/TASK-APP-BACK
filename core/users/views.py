from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from config import settings
from core.models import CustomUser
from core.users.serializer import UserRegistrationSerializer, UpdateUserSerializer, UserSerializer

def email_welcome(email):
    subject = '¡Bienvenido a nuestro sitio!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    template = get_template('emails/email-templated.html')
    context = {}
    content = template.render(context)
    email = EmailMessage(subject,content,from_email, recipient_list)
    email.content_subtype = "html"
    email.send(fail_silently=True)


class UserRegistrationView(APIView):
    """
    API endpoint for user registration.
    """

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.save()
                email_welcome(user.email)
                return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
                # return Response({"error": "Something went wrong. Please try again."},
                #                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class UserListView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        queryset = CustomUser.objects.all().order_by('-date_joined')
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)





class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)

        serializer = UpdateUserSerializer(
            user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class DeleteUserView(APIView):
    def delete(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        if not request.user.is_superuser and request.user != user:
            return Response({'detail': 'No tienes permiso para realizar esta acción.'},
                            status=status.HTTP_403_FORBIDDEN)

        user.delete()
        return Response({'message': 'User delete successfully'}, status=status.HTTP_204_NO_CONTENT)


class UserInfoView(APIView):
    # permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder a esta vista

    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)  # Obtiene el usuario por su ID
            serializer = UserSerializer(user)  # Serializa los datos del usuario
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
