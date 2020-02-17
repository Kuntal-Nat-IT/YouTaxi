from rest_framework import serializers
from ..models import PaymentHistory


class GetAllPaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = ['id', 'name', 'phoneNo', 'amountReceivable', 'amountReceived', 'dueAmount', 'timeStamp']
