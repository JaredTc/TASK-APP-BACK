from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from core.tasks.models import *
from core.tasks.serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# @permission_classes([IsAuthenticated])
class GetTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10  # 👈 tamaño de página

        queryset = Task.objects.all().order_by('-created_at')

        result_page = paginator.paginate_queryset(queryset, request)
        serializer = TasksSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)


class CreateTask(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            # Pass the user to the save method
            serializer.save(created_by=request.user)
            return Response({"message": "Task created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTask(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        task = get_object_or_404(Task,uuid=id, created_by=request.user)

        serializer = TaskSerializer(
            task,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Task updated successfully"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class createCategory(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        if isinstance(data, list):
            serializer_list = []
            for item in data:
                serializer = CategorySerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                    serializer_list.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Categories created successfully"}, status=status.HTTP_201_CREATED)
        else:
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Category created successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class createAlert(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        if isinstance(data, list):
            serializer_list = []
            for item in data:
                serializer = AlertSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                    serializer_list.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Alerts created successfully"}, status=status.HTTP_201_CREATED)
        else:
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Alert created successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class createTaskStatus(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        if isinstance(data, list):
            serializer_list = []
            for item in data:
                serializer = TaskStatusSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                    serializer_list.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Task Status created successfully"}, status=status.HTTP_201_CREATED)
        else:
            serializer = TaskStatusSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Task Status created successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class total_status(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tasks = Task.objects.all()
        to_do = tasks.filter(status=1).count()
        cancelled = tasks.filter(status=5).count()
        blocked = tasks.filter(status=3).count()
        deferred = tasks.filter(status=6).count()
        onGoing = tasks.filter(status=8).count()
        completed = tasks.filter(status=4).count()
        pending = tasks.filter(status=7).count()
        in_progress = tasks.filter(status=2).count()
        return Response({'completed': completed,
                         'Pending': pending,
                         'In Progress': in_progress,
                         'To Do': to_do,
                         'Cancelled': cancelled,
                         'Blocked': blocked,
                         'Deferred': deferred,
                         'On Going': onGoing,
                         'Completed': completed,
                         }, status=status.HTTP_200_OK)
