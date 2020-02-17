from rest_framework import serializers
from ..models import RideHistory


class GetAllRideHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RideHistory
        fields = ['id', 'name', 'phoneNo', 'startPoint', 'endPoint', 'timeStamp']
