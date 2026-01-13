from rest_framework import serializers
from core.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    imgProfile = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'is_superuser',
            'username',
            'password',
            'email',
            'is_staff',
            'is_active',
            'position',
            'imgProfile'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        img_profile = validated_data.pop('imgProfile', None)
        user = CustomUser.objects.create_user(**validated_data)

        if img_profile:
            user.imgProfile = img_profile
            user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'is_superuser',
            'username',
            'email',
            'is_staff',
            'is_active',
            'position',
            'imgProfile',
        ]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'position',
            'imgProfile',
        ]

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.position = validated_data.get('position', instance.position)
        instance.imgProfile = validated_data.get('imgProfile', instance.imgProfile)
        instance.save()
        return instance
