from rest_framework import serializers


from .models import User


# 회원 유저 목록에 출력될 형식
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'message', 'profile', ]


# 회원 가입 할 때 필요한 필드들에 대한 시리얼 라이저

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'message', 'profile', ]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()

        return user


class UserModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'first_name', 'last_name', 'email', 'message', 'profile', ]

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password' and value:
                instance.set_password(value)
            elif value:
                setattr(instance, attr, value)
        instance.save()

        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'message', 'profile',
                  'is_superuser', ]


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
