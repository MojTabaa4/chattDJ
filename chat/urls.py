from django.urls import path

from .views import ConversationView, ConversationsView

urlpatterns = [
    path('conversation/', ConversationsView.as_view(), name='conversations'),
    path('conversation/<int:pk>/', ConversationView.as_view(), name='conversation_view'),
]
