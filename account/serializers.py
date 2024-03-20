from base64 import urlsafe_b64encode
import math
import requests
from rest_framework import serializers

import otp_reg
# from otp_reg.views import generateOTP
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
# from otp_reg.views import generateOTP


class CustomUserSerializer(serializers.ModelSerializer):
    terms_and_conditions = serializers.BooleanField(default=False)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'password', 'terms_and_conditions', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError("Password and Confirm Password must match")
        
        # Create the user
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user
    
    
    
class EmployeeLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLogin
        fields = '__all__'


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'
        

class LoginProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginProfile
        fields = '__all__'
        
class EmployeeLogin2Serializer2(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLogin2
        fields = '__all__'
        
class AssignTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignTask
        fields = '__all__'


class EmployeeJoiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeJoining
        fields = '__all__'
        
        
class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUser
        fields = '__all__'

class ApplyLeavesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyLeaves
        fields = '__all__'
        
class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
        


        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class WantedApiSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = WantedApi
        fields = ['id', 'images', 'description', 'title', 'date']
        
        
class LoginProfileSerializer2(serializers.ModelSerializer):
    class Meta:
        model = LoginProfile
        fields = ['name', 'image']
          
class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'


class ImageSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Image2
        fields = ['image']

class MultiplImagesSerializer2(serializers.ModelSerializer):
    images = ImageSerializer2(many=True, read_only=True)

    class Meta:
        model = MultiplImages
        fields = '__all__'

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'
        


class ImageSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Image3
        fields = ['image']

class AdminApiSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = AdminApi
        fields = '__all__'

class TrustedCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustedCompany
        fields = '__all__'    

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectDetails
        fields='__all__'            
        
class EmployeeApproveDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= EmployeeApprovDetails
        fields='__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('email', 'otp_code')



class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, value):
        try:
            user = AdminApi.objects.get(email=value)
        except AdminApi.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return user

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")

        # Use Django's validate_password function for password validation
        try:
            validate_password(password)
        except DjangoValidationError as e:
            raise serializers.ValidationError(str(e))

        return data

    def create(self, validated_data):
        user = validated_data['email']
        password = validated_data['password']

        # Implement your logic to reset the user's password here
        user.password = password
        user.save()  # Correctly saving the user instance

        # Return the updated user instance
        return user

    


