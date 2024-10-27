from rest_framework import serializers
from .models import User, Question, UserAnswer

# Serializador para el modelo User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'image', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Usamos el método set_password para encriptar la contraseña
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Serializador para el modelo Question
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at']

# Serializador para el modelo UserAnswer
class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['id', 'user', 'question', 'answer', 'created_at']
        read_only_fields = ['user', 'created_at']
