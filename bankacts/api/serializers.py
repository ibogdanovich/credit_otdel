from rest_framework import serializers
from ..models import Action, Bank


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('shop', 'bank_id', 'last_update')

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('name', 'ext_id')
