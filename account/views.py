from django.shortcuts import render

from login_hola9 import settings
from . models import *
from . serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
import base64
from rest_framework import status
from django.http import JsonResponse
from rest_framework import generics



class RegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get('terms_and_conditions', False) is not True:
                return Response({'terms_and_conditions': ['You must accept the terms and conditions.']}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        users = User.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

class EmployeeProfileView(generics.ListCreateAPIView):
    serializer_class = EmployeeDetailsSerializer

    def get_queryset(self):
        name_param = self.request.query_params.get('name', None)
        limit = self.request.query_params.get('limit', None)
        organization_param = self.request.query_params.get('organization', None)

        queryset = EmployeeDetails.objects.all()

        if name_param and limit:
            queryset = queryset.filter(name=name_param).order_by('-id')[:int(limit)]
        elif name_param:
            queryset = queryset.filter(name=name_param)
        elif limit:
            queryset = queryset.order_by('-id')[:int(limit)]
        elif organization_param:
            queryset = queryset.filter(organization=organization_param)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
      
      
class LoginProfileList(generics.ListCreateAPIView):
    serializer_class = LoginProfileSerializer    
 
    def get_queryset(self):
            name_param = self.request.query_params.get('name', None)
            limit = self.request.query_params.get('limit', None)
            organization_param = self.request.query_params.get('organization', None)

            queryset = LoginProfile.objects.all()

            if name_param and limit:
                # If both "name" and "limit" parameters are provided,
                # filter by name first and then limit the queryset
                queryset = queryset.filter(name=name_param).order_by('-id')[:int(limit)]
            elif name_param:
                # If only "name" parameter is provided, filter by name
                queryset = queryset.filter(name=name_param)
            elif limit:
                # If only "limit" parameter is provided, order by id and limit the queryset
                queryset = queryset.order_by('-id')[:int(limit)]
            elif organization_param:
                queryset = queryset.filter(organization=organization_param)
            return queryset
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoginProfileSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'image' in request.data:
                # Get the uploaded file
                uploaded_file = request.data['image']

                # Convert the file to base64
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                # Update the serializer's data to store the base64 encoded document
                serializer.validated_data['image_base64'] = base64_encoded

            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginProfileDetail(APIView):
    def get_object(self, pk):
        try:
            return LoginProfile.objects.get(pk=pk)
        except LoginProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # Retrieve a single user profile
        profile = self.get_object(pk)
        serializer = LoginProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = LoginProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'image' in request.data:
                uploaded_file = request.data['image']
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                serializer.validated_data['image_base64'] = base64_encoded

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeLogin
from django.http import HttpResponse

class EmployeeLoginView(generics.ListCreateAPIView):
    serializer_class = EmployeeLoginSerializer

    def get_queryset(self):
        limit = self.request.query_params.get('limit', None)
        organization_param = self.request.query_params.get('organization', None)

        

        queryset = EmployeeLogin.objects.all()
        
        if limit:
            # If "limit" parameter is provided, order by id and limit the queryset
            queryset = queryset.order_by('-id')[:int(limit)]
        elif organization_param:
            queryset = queryset.filter(organization=organization_param)

        return queryset
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self,request,format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        name = request.data.get("name")
        x = EmployeeLogin.objects.filter(username=username).filter(password=password).filter(name=name)
        if x:
            return HttpResponse("true", content_type='application/json')
        else:
            return HttpResponse("false", content_type='application/json')

     
        
import base64
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EmployeeDetails
from .serializers import EmployeeDetailsSerializer

class EmployeeDetailsView(generics.ListCreateAPIView):
    serializer_class = EmployeeDetailsSerializer
    def get_queryset(self):
        limit = self.request.query_params.get('limit', None)
        name_param = self.request.query_params.get('name', None)
        organization_param = self.request.query_params.get('organization', None)



        queryset = EmployeeDetails.objects.all()
        
        if name_param and limit:
            queryset = queryset.filter(name=name_param).order_by('-id')[:int(limit)]
        elif name_param:
            queryset = queryset.filter(name=name_param)
        elif limit:
            queryset = queryset.order_by('-id')[:int(limit)]
        elif organization_param:
            queryset = queryset.filter(organization=organization_param)
        return queryset
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = EmployeeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'documnet' in request.data:
                # Get the uploaded file
                uploaded_file = request.data['documnet']

                # Convert the file to base64
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                # Update the serializer's data to store the base64 encoded document
                serializer.validated_data['document_base64'] = base64_encoded

            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmployeeLoginView2(generics.ListCreateAPIView):
    serializer_class = EmployeeLogin2Serializer2

    def get_queryset(self):
            name_param = self.request.query_params.get('name', None)
            limit = self.request.query_params.get('limit', None)
            organization_param = self.request.query_params.get('organization', None)


            queryset = EmployeeLogin2.objects.all()

            if name_param and limit:
                # If both "name" and "limit" parameters are provided,
                # filter by name first and then limit the queryset
                queryset = queryset.filter(name=name_param).order_by('-id')[:int(limit)]
            elif name_param:
                # If only "name" parameter is provided, filter by name
                queryset = queryset.filter(name=name_param)
            elif limit:
                # If only "limit" parameter is provided, order by id and limit the queryset
                queryset = queryset.order_by('-id')[:int(limit)]
            elif organization_param:
                queryset = queryset.filter(organization=organization_param)
            return queryset
            # serializer = self.get_serializer(queryset, many=True)
            # return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EmployeeLogin2Serializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  EmployeeLoginUpdateDelete2(APIView):
    def put(self,request,pk):
        employee2 = EmployeeLogin2.objects.get(pk=pk)
        serializer = EmployeeLogin2Serializer2(employee2,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self,request,pk):
        employee_login = EmployeeLogin2.objects.get(pk=pk)
        employee_login.delete()
        return Response({"message": "deleted successfully."},status=status.HTTP_204_NO_CONTENT)
    
class AssignTaskView(generics.ListCreateAPIView):
    serializer_class = AssignTaskSerializer

    def get_queryset(self):
        limit = self.request.query_params.get('limit', None)
        assignee_name = self.request.query_params.get('assignee_name', None)
        tl_name = self.request.query_params.get('tl_name', None)
        organization_param = self.request.query_params.get('organization', None)
        tester_param = self.request.query_params.get('tester', None)



        queryset = AssignTask.objects.all()
        
        if assignee_name and tl_name:
            # If "limit" parameter is provided, order by id and limit the queryset
            queryset = queryset.filter(assignee_name=assignee_name, tl_name=tl_name)
        elif assignee_name:
            queryset = queryset.filter(assignee_name=assignee_name)
        elif tl_name:
            queryset = queryset.filter(tl_name=tl_name)
        elif limit:
            queryset = queryset.order_by('-id')[:int(limit)]
        elif organization_param:
            queryset = queryset.filter(organization=organization_param)
        elif tester_param:
            queryset = queryset.filter(tester=tester_param)
        return queryset
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AssignTaskSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'add_photo' in request.data:
                # Get the uploaded file
                uploaded_file = request.data['add_photo']

                # Convert the file to base64
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                # Update the serializer's data to store the base64 encoded document
                serializer.validated_data['addphoto_base64'] = base64_encoded

            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class  AssignTaskUpdateDelete(APIView):
    def put(self,request,pk):
        assign_task = AssignTask.objects.get(pk=pk)
        serializer = AssignTaskSerializer(assign_task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self,request,pk):
        assign_task = AssignTask.objects.get(pk=pk)
        assign_task.delete()
        return Response({"message": "deleted successfully !"},status=status.HTTP_204_NO_CONTENT)
    
class adminAuth(APIView):
    def post( self,request, format=None):
        username =request.data.get("username")
        password=request.data.get("password")
        s=AdminAuth.objects.filter(username=username).filter(password=password)
        if s:
            return HttpResponse("true", content_type='application/json')
        else:
            return HttpResponse("false", content_type='application/json') 
        
# EmployeeJoiningListView

class EmployeeJoiningListView(generics.ListCreateAPIView):
    serializer_class = EmployeeJoiningSerializer
    
    def get_queryset(self):
            name_param = self.request.query_params.get('name', None)
            limit = self.request.query_params.get('limit', None)
            organization_param = self.request.query_params.get('organization', None)
            date_param =  self.request.query_params.get('dateOfJoining', None)
            month_param = self.request.query_params.get('month', None)
            year_param = self.request.query_params.get('year', None)


            queryset = EmployeeJoining.objects.all()

            if name_param and limit:
                # If both "name" and "limit" parameters are provided,
                # filter by name first and then limit the queryset
                queryset = queryset.filter(employeeName=name_param).order_by('-id')[:int(limit)]
            elif name_param:
                # If only "name" parameter is provided, filter by name
                queryset = queryset.filter(employeeName=name_param)
            elif limit:
                # If only "limit" parameter is provided, order by id and limit the queryset
                queryset = queryset.order_by('-id')[:int(limit)]
            elif organization_param:
                queryset = queryset.filter(organization=organization_param)
            elif date_param:
                queryset = queryset.filter(dateOfJoining=date_param)
            elif month_param:
                queryset = queryset.filter(month=month_param)
       
            elif year_param:
                queryset = queryset.filter(year=year_param)
            return queryset
            # serializer = self.get_serializer(queryset, many=True)
            # return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeJoiningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeJoiningDetailView(APIView):
    def get(self, request, pk):
        employee = EmployeeJoining.objects.get(pk=pk)
        serializer = EmployeeJoiningSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = EmployeeJoining.objects.get(pk=pk)
        serializer = EmployeeJoiningSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = EmployeeJoining.objects.get(pk=pk)
        employee.delete()
        return Response({"message": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



class AddUserList(APIView):
    def get(self, request):
        users = AddUser.objects.all()
        serializer = AddUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddUserDetail(APIView):
    def get_object(self, pk):
        try:
            return AddUser.objects.get(pk=pk)
        except AddUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = AddUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = AddUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ApplyLeavesList(APIView):
    def get(self, request):
        leaves = ApplyLeaves.objects.all()
        serializer = ApplyLeavesSerializer(leaves, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplyLeavesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplyLeavesDetail(APIView):
    def get_object(self, pk):
        try:
            return ApplyLeaves.objects.get(pk=pk)
        except ApplyLeaves.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        leave = self.get_object(pk)
        serializer = ApplyLeavesSerializer(leave)
        return Response(serializer.data)

    def put(self, request, pk):
        leave = self.get_object(pk)
        serializer = ApplyLeavesSerializer(leave, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        leave = self.get_object(pk)
        leave.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MediaList(APIView):
    def get(self, request):
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MediaDetail(APIView):
    def get_object(self, pk):
        try:
            return Media.objects.get(pk=pk)
        except Media.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        media = self.get_object(pk)
        serializer = MediaSerializer(media)
        return Response(serializer.data)

    def put(self, request, pk):
        media = self.get_object(pk)
        serializer = MediaSerializer(media, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        media = self.get_object(pk)
        media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    





class WantedApiCreateAPIView(APIView):
    def post(self, request, format=None):
        # Serialize the data from the request
        your_model_serializer = WantedApiSerializer(data=request.data)

        # Check if the data is valid
        if your_model_serializer.is_valid():
            # Save the YourModelName instance
            your_model_instance = your_model_serializer.save()

            # Handle the images
            images_data = request.FILES.getlist('images')  # Get uploaded images
            for image_data in images_data:
                # Serialize each image
                image_serializer = ImageSerializer(data={'image': image_data})
                if image_serializer.is_valid():
                    # Save the image and associate it with the YourModelName instance
                    image_serializer.save()
                    your_model_instance.images.add(image_serializer.instance)
                else:
                    # If any image serialization fails, delete the YourModelName instance
                    your_model_instance.delete()
                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(your_model_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(your_model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        # Retrieve all instances of WantedApiModel and serialize them
        wanted_instances = WantedApi.objects.all()
        serializer = WantedApiSerializer(wanted_instances, many=True)
        return Response(serializer.data)




class FeedList(APIView):
   
    def get(self, request):
        feeds = Feed.objects.all()
        feed_data = []
        for feed in feeds:
            serializer = FeedSerializer(feed)
            try:
                profile = LoginProfile.objects.get(name=feed.name)
                profile_serializer = LoginProfileSerializer2(profile)
                feed_data.append({
                    **serializer.data,
                    'profile': profile_serializer.data
                })
            except LoginProfile.DoesNotExist:
                feed_data.append({
                    **serializer.data,
                    'profile': {'name': None, 'image': None}
                })
        return Response(feed_data)


    def post(self, request):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FeedsUpdateDelete(APIView):
    def delete(self,request,pk):
        feed = Feed.objects.get(pk=pk)
        feed.delete()
        return Response({"Message":"Delete Feed Successfully !!"},status=status.HTTP_204_NO_CONTENT)
    
class MultiplImageView(APIView):
    def post(self, request, format=None):
        # Serialize the data from the request
        your_model_serializer = MultiplImagesSerializer2(data=request.data)

        # Check if the data is valid
        if your_model_serializer.is_valid():
            # Save the YourModelName instance
            your_model_instance = your_model_serializer.save()

            # Handle the images
            images_data = request.FILES.getlist('images')  # Get uploaded images
            for image_data in images_data:
                # Serialize each image
                image_serializer = ImageSerializer2(data={'image': image_data})
                if image_serializer.is_valid():
                    # Save the image and associate it with the YourModelName instance
                    image_serializer.save()
                    your_model_instance.images.add(image_serializer.instance)
                else:
                    # If any image serialization fails, delete the YourModelName instance
                    your_model_instance.delete()
                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(your_model_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(your_model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, format=None):
        # Retrieve all instances of WantedApiModel and serialize them
        wanted_instances = MultiplImages.objects.all()
        serializer = MultiplImagesSerializer2(wanted_instances, many=True)
        return Response(serializer.data)
    
class MultiplImageUpdateDelete(APIView):
    def put(self,request,pk):
        img=MultiplImages.objects.get(pk=pk)
        serializer = MultiplImagesSerializer2(img,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        img=MultiplImages.objects.get(pk=pk)
        img.delete()
        return Response({"Message":"Data Delete Successfully!!"},status=status.HTTP_204_NO_CONTENT)    






class HolidayListView(generics.ListCreateAPIView):
    serializer_class = HolidaySerializer
    
    def get_queryset(self):
            organization_param = self.request.query_params.get('organization', None)
            queryset = Holiday.objects.all()
            if organization_param:
                queryset = queryset.filter(organization=organization_param)
            return queryset
        
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HolidaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class HolidayDetailView(APIView):
    def get_object(self, pk):
        try:
            return Holiday.objects.get(pk=pk)
        except Holiday.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        holiday = self.get_object(pk)
        serializer = HolidaySerializer(holiday, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        holiday = self.get_object(pk)
        holiday.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CheckLoginLogoutAvailability(APIView):
#     def get(self, request):
#         try:
#             # Retrieve all EmployeeLogin2 objects
#             all_employee_data = EmployeeLogin2.objects.all()

#             # Filter EmployeeLogin2 objects where logout_time - login_time is less than 8 hours
#             filtered_employee_data = []
#             for employee_data in all_employee_data:
#                 login_time_str = employee_data.login_time
#                 logout_time_str = employee_data.logout_time

#                 # Check if login_time or logout_time is empty
#                 if login_time_str is None or logout_time_str is None:
#                     continue  # Skip this entry if either login_time or logout_time is empty

#                 login_time = datetime.strptime(login_time_str, "%I:%M:%S %p")
#                 logout_time = datetime.strptime(logout_time_str, "%I:%M:%S %p")
#                 duration = logout_time - login_time
#                 if duration < timedelta(hours=8):
#                     filtered_employee_data.append(employee_data)

#             # Retrieve data where either login_time or logout_time is null
#             null_time_data = EmployeeLogin2.objects.filter(login_time__isnull=True) | \
#                              EmployeeLogin2.objects.filter(logout_time__isnull=True)

#             # Serialize the filtered employee data
#             serializer = EmployeeLogin2Serializer2(filtered_employee_data, many=True)

#             # Serialize the data where login_time or logout_time is null
#             null_time_serializer = EmployeeLogin2Serializer2(null_time_data, many=True)

#             # Combine both sets of data
#             response_data = {
#                 'below_8_hr_data': serializer.data,
#                 'null_time_data': null_time_serializer.data
#             }

#             return Response(response_data, status=status.HTTP_200_OK)
#         except EmployeeLogin2.DoesNotExist:
#             return Response({'error': 'Employee data not found.'}, status=status.HTTP_404_NOT_FOUND)



class CheckLoginLogoutAvailability(APIView):
    def get(self, request):
        try:
            # Get the name parameter from the request query parameters
            name = request.query_params.get('name')

            if name:
                # Check if the provided name exists in the EmployeeLogin2 objects
                if EmployeeLogin2.objects.filter(name=name).exists():
                    # If the name exists, filter EmployeeLogin2 objects by name
                    all_employee_data = EmployeeLogin2.objects.filter(name=name)
                else:
                    # If the name does not exist, return an empty response
                    return Response({'error': f'Employee with name {name} not found.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                # If no name is provided, retrieve all EmployeeLogin2 objects
                all_employee_data = EmployeeLogin2.objects.all()

            # Filter EmployeeLogin2 objects where logout_time - login_time is less than 8 hours
            filtered_employee_data = []
            for employee_data in all_employee_data:
                login_time_str = employee_data.login_time
                logout_time_str = employee_data.logout_time

                # Check if login_time or logout_time is empty
                if login_time_str is None or logout_time_str is None:
                    continue  # Skip this entry if either login_time or logout_time is empty

                login_time = datetime.strptime(login_time_str, "%H:%M%S")
                logout_time = datetime.strptime(logout_time_str, "%H:%M%S")
                duration = logout_time - login_time
                if duration < timedelta(hours=8):
                    filtered_employee_data.append(employee_data)

            # Retrieve data where either login_time or logout_time is null
            null_time_data = EmployeeLogin2.objects.filter(login_time__isnull=True) | \
                             EmployeeLogin2.objects.filter(logout_time__isnull=True)

            # Serialize the filtered employee data
            serializer = EmployeeLogin2Serializer2(filtered_employee_data, many=True)

            # Serialize the data where login_time or logout_time is null
            null_time_serializer = EmployeeLogin2Serializer2(null_time_data, many=True)

            # Combine both sets of data
            response_data = {
                'filtered_employee_data': serializer.data,
                'null_time_data': null_time_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except EmployeeLogin2.DoesNotExist:
            return Response({'error': 'Employee data not found.'}, status=status.HTTP_404_NOT_FOUND)






# class AdminApiList(APIView):

#     def post(self, request, format=None):
#         # Serialize the data from the request
#         your_model_serializer = AdminApiSerializer(data=request.data)

#         # Check if the data is valid
#         if your_model_serializer.is_valid():
#             # Save the YourModelName instance
#             your_model_instance = your_model_serializer.save()

#             # Handle the images
#             images_data = request.FILES.getlist('images')  # Get uploaded images
#             for image_data in images_data:
#                 # Serialize each image
#                 image_serializer = ImageSerializer(data={'image': image_data})
#                 if image_serializer.is_valid():
#                     # Save the image and associate it with the YourModelName instance
#                     image_serializer.save()
#                     your_model_instance.images.add(image_serializer.instance)
#                 else:
#                     # If any image serialization fails, delete the YourModelName instance
#                     your_model_instance.delete()
#                     return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#             return Response(your_model_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(your_model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminApiList(APIView):

    def post(self, request, format=None):
        # Serialize the data from the request
        your_model_serializer = AdminApiSerializer(data=request.data)

        # Check if the data is valid
        if your_model_serializer.is_valid():
            # Save the YourModelName instance
            your_model_instance = your_model_serializer.save()
            
            
            # Extract relevant data
            username = your_model_instance.user_id
            password = your_model_instance.password
            name = your_model_instance.name
            organization = your_model_instance.organization

            # Create AdminAuth instance
            admin_auth_instance = AdminAuth.objects.create(username=username, password=password, name=name, organization=organization)
            # Handle the images
            images_data = request.FILES.getlist('images')  # Get uploaded images
            for image_data in images_data:
                # Serialize each image
                image_serializer = ImageSerializer(data={'image': image_data})
                if image_serializer.is_valid():
                    # Save the image and associate it with the YourModelName instance
                    image_serializer.save()
                    your_model_instance.images.add(image_serializer.instance)
                else:
                    # If any image serialization fails, delete the YourModelName instance
                    your_model_instance.delete()
                    admin_auth_instance.delete()

                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(your_model_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(your_model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AdminApiGet(generics.ListCreateAPIView):
    serializer_class = AdminApiSerializer

    def get_queryset(self):
        organization_param = self.request.query_params.get('organization', None)
        queryset = AdminApi.objects.all()
        if organization_param:
            queryset = queryset.filter(organization=organization_param)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class AdminApiUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return AdminApi.objects.get(pk=pk)
        except AdminApi.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        media = self.get_object(pk)
        serializer = AdminApiSerializer(media)
        return Response(serializer.data)

    def put(self, request, pk):
        media = self.get_object(pk)
        serializer = AdminApiSerializer(media, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        media = self.get_object(pk)
        media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class TrustedComapnyView(APIView):
    def get(self,request,format=None):
        com=TrustedCompany.objects.all()
        serializer=TrustedCompanySerializer(com,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)    
    
    def post(self,request,format=None):
        serializer = TrustedCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TrustedCompanyUpdateDelete(APIView):
    def put(self,request,pk):
          com=TrustedCompany.objects.get(pk=pk)
          serializer = TrustedCompanySerializer(com,data=request.data, partial=True)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        com=TrustedCompany.objects.get(pk=pk)
        com.delete()
        return Response({"Message":"Delete Successfully !!!"},status=status.HTTP_204_NO_CONTENT)
    
class ProjectDetailsView(APIView):
    def get(self, request):
        pro = ProjectDetails.objects.all()
        pro_data = []

        for pro_details in pro:
            serializer = ProjectDetailSerializer(pro_details)
            
            employeename_list = pro_details.employeename.split(',')

            tl_data = {'name': None, 'image': None}
            emp_profiles = []

            for emp_name in employeename_list:
                try:
                    profile = LoginProfile.objects.get(name=emp_name.strip())
                    profile_serializer = LoginProfileSerializer2(profile)

                    # Check if the employee is a TL based on the 'tl' field
                    if profile.role == 'tl':
                        tl_data = {
                            'name': profile.name,
                            'image': profile.image.url if profile.image else None
                        }
                    else:
                        emp_profiles.append({
                            'name': profile.name,
                            'image': profile.image.url if profile.image else None
                        })
                except LoginProfile.DoesNotExist:
                    pass

            pro_data.append({
                **serializer.data,
                'tl': tl_data,
                'emp_profiles': emp_profiles
            })

        return Response(pro_data)
    
    def post(self,request,format=None):
        serializer = ProjectDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProjectDetailsUpdateDelete(APIView):
    def put (self,request,pk):
        proj=ProjectDetails.objects.get(pk=pk)
        serializer = ProjectDetailSerializer(proj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        proj=ProjectDetails.objects.get(pk=pk)
        proj.delete()
        return Response({"Message":"Project Details Delete Successfully!!"},status=status.HTTP_204_NO_CONTENT)  

class EmployeeApproveDetailView(APIView):
    def get (self,request,format=None):
        emp=EmployeeApprovDetails.objects.all()
        serializer = EmployeeApproveDetailsSerializer(emp,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = EmployeeApproveDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeAprroveUpdateDelete(APIView):
    def put(self,request,pk):
        emp =EmployeeApprovDetails.objects.get(pk=pk)
        serializer = EmployeeApproveDetailsSerializer(emp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        emp=EmployeeApprovDetails.objects.get(pk=pk)
        emp.delete()
        return Response({"Message":"Delete Successfully!!"},status=status.HTTP_204_NO_CONTENT)
    
class ForgotAdminPasswordView(APIView):
    def post(self, request, format=None):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Implement your logic to reset the user's password here
        user = serializer.save()

        # You can include additional information in the response as needed
        return Response({"detail": "Password reset successful.","new_password": user.password},status=status.HTTP_200_OK)
# from account.utils import create_notification_functions
class NotificationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        if name:
            notifications = Notifications.objects.filter(name=name)
        else:
            notifications = Notifications.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
        

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OTP
from .serializers import OTPSerializer
from django.core.mail import send_mail
# from django.conf import settings
import random


class SendOTP(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)


        # Generate OTP
        otp_code = ''.join(random.choices('0123456789', k=6))


        # Save OTP to database
        otp_instance = OTP.objects.create(email=email, otp_code=otp_code)


        # Send OTP via email
        send_mail(
            'Your OTP',
            f'Your OTP is: {otp_code}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )


        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)


class VerifyOTP(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp_code = request.data.get('otp_code')


        if not email or not otp_code:
            return Response({'error': 'Email and OTP code are required'}, status=status.HTTP_400_BAD_REQUEST)


        # Check if OTP exists
        try:
            otp_instance = OTP.objects.get(email=email, otp_code=otp_code)
        except OTP.DoesNotExist:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)


        # If OTP is valid, delete it from the database
        # otp_instance.delete()
        otp_instance.is_verified = True
        otp_instance.save()


        return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)



    
    