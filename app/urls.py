from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, QuestionViewSet, UserAnswerViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'answers', UserAnswerViewSet, basename='answer')

urlpatterns = [
    path('api/', include(router.urls)),
]
