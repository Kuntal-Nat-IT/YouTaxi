from rest_framework import serializers
from YouTaxiDriver.models import Driver
from YouTaxiUser.models import User


class CreateDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['firstName', 'lastName', 'phoneNo', 'email', 'preferedHour', 'cityOfWork', 'LinkedTaxiLicense']


class GetAllDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'firstName', 'lastName', 'phoneNo', 'email', 'status']


class GetDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'firstName', 'lastName', 'countryCode', 'phoneNo', 'email', 'address', \
            'landLineNumber', 'dateOfBirth', 'placeOfBirth', 'createDate', 'removeDate',\
            'DNIAddress', 'DNICityAddress', 'ExpirationDateCirculationPermit', 'Regularschedule', \
            'LinkedTaxiLicense', 'RegistrationTaxiLinked', 'language', 'AdminNotices', \
            'TravelCommission', 'CommissionChargeCards', 'BankCurrentAccount', 'AdminNotes',\
            'profileImg', 'PhotoDNI', 'CredintialPhoto', 'preferedHour', 'cityOfWork', \
            'comisionTpv', 'BankAccountDetails', 'driverScore', 'status']


class UpdateDriverDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['firstName', 'lastName', 'address', 'landLineNumber', 'dateOfBirth', 'placeOfBirth', 'DNIAddress', \
            'DNICityAddress', 'LinkedTaxiLicense', 'RegistrationTaxiLinked', 'AdminNotices', \
            'TravelCommission', 'CommissionChargeCards', 'BankCurrentAccount', 'AdminNotes',\
            'preferedHour', 'cityOfWork', 'comisionTpv', 'BankAccountDetails']


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullName', 'countryCode', 'phoneNo', 'email', 'createDate', \
            'status', 'isDeleted', 'dateOfBirth', 'gender', 'address', 'language', \
            'favoriteTaxis', 'taxisBlocked', 'adminNotices', 'package', 'solidarityTaxi', 'handicapedTaxi', \
            'bankCardDetails', 'bankAccountDetails', 'typeOfClient']