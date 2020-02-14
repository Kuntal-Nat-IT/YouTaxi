from rest_framework import serializers
from ..models import Admin
from YouTaxiUser.models import User
from YouTaxiDriver.models import Driver


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['firstName', 'lastName', 'email', 'password', 'phoneNo', 'address', 'role', 'resetPasswordToken', 'tokenExpiration']


class GetAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['firstName', 'lastName', 'email', 'phoneNo', 'address', 'role']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fullName', 'countryCode', 'phoneNo', 'typeOfClient', 'email', 'status', 'package', 'solidarityTaxi', 'handicapedTaxi']


class CreateUserByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fullName', 'countryCode', 'phoneNo', 'email', 'createDate', 'removeDate',\
            'status', 'dateOfBirth', 'gender', 'address', 'adminNotices', \
            'typeOfClient', 'solidarityTaxi', 'handicapedTaxi', 'package']



class CreateDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['firstName', 'lastName', 'phoneNo', 'email', \
            'CredintialPhoto', 'preferedHour']


class CreateDriverByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['firstName', 'lastName', 'phoneNo', 'email', 'createDate', 'removeDate', 'TravelCommission', \
                'preferedHour', 'comisionTpv', 'BankAccountDetails', 'TravelCommission', 'CommissionChargeCards',\
                'BankCurrentAccount']