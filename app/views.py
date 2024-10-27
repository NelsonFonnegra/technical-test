from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import User, Question, UserAnswer
from .serializers import UserSerializer, QuestionSerializer, UserAnswerSerializer

# ViewSet para el modelo User (manejo de registro y perfil de usuario)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], permission_classes=[])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Usuario registrado exitosamente"}, status=status.HTTP_201_CREATED)

# ViewSet para el modelo Question (manejo de preguntas personalizadas)
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para el modelo UserAnswer (manejo de respuestas del usuario)
class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Asigna automáticamente el usuario autenticado a la respuesta
        serializer.save(user=self.request.user)
