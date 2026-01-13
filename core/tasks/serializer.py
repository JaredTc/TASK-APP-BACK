from rest_framework import serializers

from core.models import CustomUser
from core.tasks.models import TaskStatus, Task, Category, Alert


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = [
            'id',
            'name',
            'description'
        ]

    def create(self, validated_data):
        status = TaskStatus.objects.create(**validated_data)
        return status


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'uuid',
            'title',
            'date_end',
            'assigned_to',
            'description',
            'category',
            'status',
            'is_completed',
            'alerts',
            'objective',
            'percent',
        ]

    def create(self, validated_data):
        # Get the user from the context
        user = self.context.get('user')
        if user:
            validated_data['created_by'] = user
        return super().create(validated_data)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = [
            'id',
            'name',
            'description'
        ]


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = [
            'id',
            'name',
            'description',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']  # Mostrar solo el nombre de usuario


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']  # Mostrar solo el nombre de la categoría


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['name']  # Mostrar solo el nombre del estado de tarea


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['name']  # Mostrar solo


class TasksSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)
    assigned_to = serializers.CharField(source='assigned_to.username')
    created_by = serializers.CharField(source='created_by.username')
    category = serializers.CharField(source='category.name')
    status = serializers.CharField(source='status.name')
    alerts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Task
        fields = [
            'uuid',
            'title',
            'date_end',
            'assigned_to',
            'description',
            'category',
            'status',
            'is_completed',
            'alerts',
            'created_by',
            'objective',
            'percent',
            'created_at',
            'updated_at'
        ]
