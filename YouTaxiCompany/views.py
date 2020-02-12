'''
        view.py
   @ Author  Kuntal
   @ Company Nat It Solved Pvt Ltd
   @ version  0.1
   @date      10/12/2019
'''

# Django Import
from django.conf import settings
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
import datetime
import json
from django.contrib.auth import authenticate

# Model Import
from .models import Company, Workers

# Serializers Import
from .serializers import companySerializers


# Rest Framework
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes



@api_view(['POST'])
def CreateCompany(request):
        try:
                # name = request.data['name']
                # address = request.data['address']
                # city = request.data['city']
                # postalCode = request.data['postalCode']
                # nif = request.data['nif']
                # administrators = request.data['administrators']
                # bankCardDetails = request.data['bankCardDetails']
                # bankAccountDetails = request.data['bankAccountDetails']
                # phoneNo = request.data['phoneNo']
                # firstName = request.data['firstName']
                # lastName = request.data['lastName']
                # email = request.data['email']

                # WorkerObject = Workers(phoneNo=phoneNo,firstName=firstName,lastName=lastName,email=email)
                # WorkerObject.save()

                # CompanyObject = Company(name=name,address=address,city=city,postalCode=postalCode,\
                #         nif=nif,administrators=administrators,Worker=WorkerObject,bankCardDetails=bankCardDetails,\
                #         bankAccountDetails=bankAccountDetails)
                # Company.save()
                
                # print(request.data)
                C = companySerializers.CreateCompanySerializer(data=request.data)
                if C.is_valid(raise_exception=True):
                        C.save()

                success = True
                status = 201
                ack = 5
                msg = "Successfully Created"
        except Exception as e:
                print("CreateCompany : ", e)
                success = False
                status = 400
                ack = 1
                msg = "Fail To Create Company"
        data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
        return Response(data, status=status)


@api_view(['GET'])
def GetAllCompany(request):
        try:
                CompanyObject = Company.objects.all().filter(isDeleted=False)
                companyList = companySerializers.GetAllCompanySerializers(CompanyObject, many=True)
                companyList = companyList.data
                success = True
                status = 200
                ack = 5
                msg = "Data Loaded"
        except Exception as e:
                print("GetAllCompany : ", e)
                companyList = []
                success = False
                status = 400
                ack = 1
                msg = "Fail To Load"

        data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'companyList': companyList}
        return Response(data, status=status)


@api_view(['GET'])
def GetCompanyByID(request, slug):
        try:
                companyObject = Company.objects.get(id=slug)
                companyData = companySerializers.GetCompanyByIdSerializers(companyObject, many=False)
                companyData = companyData.data
                success = True
                status = 200
                ack = 5
                msg = "Data Loaded"
        except Exception as e:
                print("GetCompanyByID : ", e)
                companyData = {}
                success = False
                status = 400
                ack = 1
                msg = "Fail To Load"

        data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'driverData': companyData}
        return Response(data, status=status)


@api_view(['POST'])
def UpdateCompanyByID(request, slug):
        try:
                companyObject = Company.objects.get(id=slug)
                try:
                        address = request.data['address']
                except Exception as e:
                        address = ''
                try:
                        city = request.data['city']
                except:
                        city = ''
                try:
                        postalCode = request.data['postalCode']
                except:
                        postalCode = ''
                try:
                        nif = request.data['nif']
                except:
                        nif = ''
                try:
                        administrators = request.data['administrators']
                except:
                        administrators = ''
                try:
                        addDate = request.data['addDate']
                except:
                        addDate
                try:
                        removeDate = request.data['removeDate']
                except:
                        removeDate = ''
                try:
                        bankCardDetails = request.data['bankCardDetails']
                except:
                        bankCardDetails = ''
                try:
                        bankAccountDetails = request.data['bankAccountDetails']
                except:
                        bankAccountDetails = ''
                try:
                        status = request.data['status']
                except:
                        status = ''
                if address != '':
                        companyObject.address = address
                if city != '':
                        companyObject.city = city
                if postalCode != '':
                        companyObject.postalCode = postalCode
                if nif != '':
                        companyObject.nif = nif
                if administrators != '':
                        companyObject.administrators = administrators
                if addDate != '':
                        companyObject.addDate = addDate
                if removeDate != '':
                        companyObject.removeDate = removeDate
                if bankCardDetails != '':
                        companyObject.bankCardDetails = bankCardDetails
                if bankAccountDetails != '':
                        companyObject.bankAccountDetails = bankAccountDetails
                if address != '':
                        companyObject.status = status
                companyObject.save()
                
                success = True
                status = 200
                ack = 5
                msg = "Data Loaded"
        except Exception as e:
                print("UpdateCompanyByID : ", e)
                success = False
                status = 400
                ack = 1
                msg = "Fail To Load"

        data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
        return Response(data, status=status)


@api_view(['POST'])
def ChangeStatus(request, slug):
        try:
                companyObject = Company.objects.get(id=slug)
                if companyObject.status:
                        companyObject.status = False
                else:
                        companyObject.status = True
                companyObject.save()

                success = True
                status = 200
                ack = 5
                msg = "Status Changed"
        except Exception as e:
                print("ChangeStatus : ", e)
                success = False
                status = 400
                ack = 1
                msg = "Fail To Change Status"

        data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
        return Response(data, status=status)


@api_view(['POST'])
def ActivateDactivate(request, slug):
        try:
                companyObject = Company.objects.get(id=slug)
                companyObject.isDeleted = True
                companyObject.save()
                
                success = True
                status = 200
                ack = 5
                msg = "Deleted"
        except Exception as e:
                print("ChangeStatus : ", e)
                success = False
                status = 400
                ack = 1
                msg = "Fail To Delete"

        data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
        return Response(data, status=status)