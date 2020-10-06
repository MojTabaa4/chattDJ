from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status

from .serializers import (UpdateMessageMessageSerializer,
                          CreatedMessageSerializers,
                          ConversationListSerializer,
                          MessageSerializer)
from .models import Message, Conversation


class ConversationsView(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        conversation = Conversation.objects.all()
        return Response(ConversationListSerializer(conversation, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ConversationListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'conversation created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'validation failed'}, status=status.HTTP_400_BAD_REQUEST)


class ConversationView(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request, pk):
        message = Message.objects.filter(conversation_id=pk).all()
        return Response(MessageSerializer(message, many=True).data)

    def post(self, request, pk):
        conversation = Conversation.objects.filter(conversation_id=pk)
        serializer = CreatedMessageSerializers(data=request.data, context={'sender': request.user,
                                                                           'conversation': conversation})
        if serializer.is_valid():
            serializer.save(sender=request.user, conversation=conversation)
            return Response({'message': 'message created'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'validation failed',
                             'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        message = Message.objects.get(id=request.data['id'])
        serializer = UpdateMessageMessageSerializer(message, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'message updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'validation failed',
                             'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
