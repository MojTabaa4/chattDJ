from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Message, Conversation


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class CreatedMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text']

    def validate(self, attrs):
        if self.context['sender'] not in self.context['conversation'].member.all():
            raise ValidationError("you are not a member of this conversation")
        return attrs


class UpdateMessageMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text']


class ConversationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'name', 'members']
