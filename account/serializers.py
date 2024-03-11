from rest_framework import serializers
from .models import *



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