import hashlib
import binascii
import jwt
import random
from math import radians, cos, sin, asin, sqrt 

from django.conf import settings
from twilio.rest import Client
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as user_models
from . import serializers as user_serializer
from Client import models as client_models
from Client import serializers as client_serializer
from Shop import models as shop_models
from Shop import serializers as shop_serializer


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def create_jwt(user_obj):
    """Function for creating JWT for Authentication Purpose"""
    return jwt.encode(
        user_serializer.GetUserInfoSerializer(user_obj).data,
        settings.SECRET_KEY, algorithm='HS256').decode('utf-8')


class RegisterUser(generics.CreateAPIView):
    def post(self, request):
        data = self.request.data    
        valid_keys = ['name','mobile','password','email']
        for key in valid_keys:
            if not key in data:
                return Response({
                    "message": key + " is missing"
                }, status=status.HTTP_400_BAD_REQUEST)

        new_user = (user_models.User.objects.filter(mobile=data['mobile']).first()
            | user_models.User.objects.filter(email=data['email']).first())
        if not new_user:
            user = user_models.User(
                name=data['name'],
                mobile=data['mobile'],
                password=data['password'],
                email=data['email']
            )
            user.save()
            user = user_models.User.objects.filter(mobile=data['mobile']).first()
            client_user = client_models.Client(user=user)
            client_user.save()
        else:
            return Response({
                "message": "User with this credentials already exist!"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'message': 'Register Succesfully',
            'user_id': client_user.pk
        }, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        data = self.request.data
        valid_keys = ['email','password','latitude', 'longitude']
        for key in valid_keys:
            if not key in data:
                return Response({
                    "message": key + " is missing"
                }, status=status.HTTP_400_BAD_REQUEST)

        user = user_models.User.objects.filter(email=data['email']).first()
        if user:
            if verify_password(user.password, data['password']):
                user.auth_token = ""
                user.save()
                jwt_token = create_jwt(user)
                user.auth_token = jwt_token
                user.save()
                client = client_models.Client.objects.filter(user=user).first()
                if not client:
                    return Response({
                        "message": "Invalid Client"
                    }, status=status.HTTP_400_BAD_REQUEST)
                return Response({
                    'message': 'Login Succesfully',
                    'token':jwt_token,
                    'client': client_serializer.GetClientInfoSerializer(client).data,
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'message': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                    {'message': 'User not exist with this mobile number'}, status=status.HTTP_400_BAD_REQUEST)


class CheckMobileNumber(APIView):
    def post(self, request):
        if not 'mobile_number' in self.request.data:
            return Response({
                "message": "Mobile Number Missing"
            }, status=status.HTTP_400_BAD_REQUEST)
        mobile_number = self.request.data['mobile_number']

        obj = models.User.objects.filter(mobile=mobile_number).first()
        if obj:
            return Response({
                "message": 'User already Exists',
                'is_valid' : True},
                status=status.HTTP_200_OK)
        return Response({
            "message": "User didn't Exists",
            'is_valid' : False},
            status=status.HTTP_200_OK)


class SendOTP(APIView):
    def post(self, request):
        if not 'mobile_number' in self.request.data:
            return Response({
                "message": "Mobile Number Missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        mobile_number = self.request.data['mobile_number']
        otp = random.randrange(1000,9999)
        obj = user_models.MobileNumberOTP.objects.filter(mobile=mobile_number).first()
        if obj:
            obj.otp = otp
        else:
            obj = user_models.MobileNumberOTP(mobile=mobile_number, otp=otp)
        obj.save()

        account_sid = 'AC628d6956958a0f43a8e3ccd0107a45e2'
        auth_token = '386e8305df56d14a2df95ed73a819aa1'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=str(otp),
            from_='+14782460432',
            to=mobile_number
        )
        return Response({
            "message": 'OTP Sent Succesfully',
            'otp': str(otp)
        }, status=status.HTTP_200_OK)


class VerifyOTP(APIView):
    def post(self, request):
        data = self.request.data
        valid_keys = ['mobile', 'otp']
        for key in valid_keys:
            if not key in data:
                return Response({
                    "message": key + " is missing"
                }, status=status.HTTP_400_BAD_REQUEST)

        mobile_number = self.request.data['mobile']
        obj = user_models.MobileNumberOTP.objects.filter(mobile=mobile_number).first()

        if not obj:
            return Response({
                "message": "Number Not Verified, Send OTP again on this number"
            }, status=status.HTTP_400_BAD_REQUEST)
        if obj.otp != self.request.data['otp']:
            return Response({
                "message": "Invalid OTP"
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": 'Verified Succesfully',
        }, status=status.HTTP_200_OK)


class ChangeUserPassword(APIView):
    def post(self, request):
        data = self.request.data
        valid_keys = ['mobile', 'old_password', 'new_password']
        for key in valid_keys:
            if not key in data:
                return Response({
                    "message": key + " is missing"
                }, status=status.HTTP_400_BAD_REQUEST)

        user = user_models.User.objects.filter(mobile=data['mobile']).first()
        if not user:
            return Response({"message": "No User exists with this mobile number"})
        if verify_password(user.password, self.request.data['old_password']):
            user.password = self.request.data['new_password']
            user.save()
            return Response({"message": "Password changed Succesfully"})
        return Response({"message": "Invalid Old Password"})
