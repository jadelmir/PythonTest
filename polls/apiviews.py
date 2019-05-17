from rest_framework import generics , viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Poll, Choice,Events
from django.contrib.auth.models import User
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer,UserSerializer,EventsSerializer
from rest_framework.parsers import FormParser
class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer


class CreateVote(APIView):

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class UserCreate(generics.CreateAPIView):
    parser_classes = (FormParser,)
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()
    parser_classes = (FormParser,)


    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key , "ID":user.id})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UsersView(viewsets.ModelViewSet):
    permission_classes = ()

    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventsView(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class UserEventsView(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return Events.objects.filter(id=user)