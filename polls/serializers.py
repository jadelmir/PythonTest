from rest_framework import serializers
from .models import Poll, Choice, Vote,Events
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('username', 'email', 'password')
            extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user
            # headers = self.get_success_headers(serializer.data)
            # return Response(
            #  {"Success": "Data posted successfully"},
            #  status=status.HTTP_201_CREATED)


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events 
        fields = '__all__'