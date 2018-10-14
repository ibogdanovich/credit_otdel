from rest_framework import generics
from ..models import Action, Bank
from .serializers import ActionSerializer, BankSerializer


class ActionListView(generics.ListAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class ActionDetailView(generics.ListAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class BankListView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer