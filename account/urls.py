from django.urls import path
from .views import  *
from account.views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('register/', RegistrationView.as_view(), name='register'),
     path('employeeprofile/', EmployeeProfileView.as_view(), name='employeeprofile'),# done
     path('loginprofile/', LoginProfileList.as_view(), name='loginprofile'),# done
     path('loginprofile/<int:pk>/', LoginProfileDetail.as_view(), name='profile-detail'), #done
     path('loginEmployee/', EmployeeLoginView.as_view(), name='loginEmployee'),# done
     path('detailEmployee/', EmployeeDetailsView.as_view(), name='detailEmployee'),# done
     path('employeelogin2',EmployeeLoginView2.as_view(), name='employeelogin2'),# done
     path('employeelogin2/<int:pk>',EmployeeLoginUpdateDelete2.as_view(), name='employeelogin2'),# done
     path('assigntaskview',AssignTaskView.as_view(), name='assigntaskview'), # done
     path('assigntaskview/<int:pk>',AssignTaskUpdateDelete.as_view(), name='assigntaskview'), # done
     path('adminAuth', adminAuth.as_view(),name='adminAuth'), # done
     
     path('employees_joining/', EmployeeJoiningListView.as_view(), name='employees_joining'), # done
     path('employees_joining/<int:pk>/', EmployeeJoiningDetailView.as_view(), name='employees_joining-detail'),

     path('adduser/', AddUserList.as_view(), name='add_user_list'),
     path('adduser/<int:pk>/', AddUserDetail.as_view(), name='add_user_detail'),
     
     path('leaves/', ApplyLeavesList.as_view(), name='apply_leaves_list'),
     path('leaves/<int:pk>/', ApplyLeavesDetail.as_view(), name='apply_leaves_detail'),

     path('media/', MediaList.as_view(), name='media-list'),
     path('media/<int:pk>/', MediaDetail.as_view(), name='media-detail'),

     path('wanted/', WantedApiCreateAPIView.as_view(), name='wanted'),
     
     path('feeds/', FeedList.as_view(), name='feed'),
     path('feeds/<int:pk>/', FeedsUpdateDelete.as_view(), name='feed'),

     path('multiplimage/', MultiplImageView.as_view(), name='multiplimage'),
     path('multiplimage/<int:pk>/', MultiplImageUpdateDelete.as_view(), name='multiplimage'),

     path('holiday/', HolidayListView.as_view(), name='holiday'),
     path('holiday/<int:pk>/', HolidayDetailView.as_view(), name='holiday-detail'),

     path('datamissing/', CheckLoginLogoutAvailability.as_view(), name='datamissing'),
     
     path('adminapi/', AdminApiList.as_view(), name='adminapi'),
     path('adminapiget/', AdminApiGet.as_view(), name='adminapiget'),
     path('adminapiupdate/<int:pk>/', AdminApiUpdateDelete.as_view(), name='adminapiupdate'), 
         
     path('trustedcompany/', TrustedComapnyView.as_view(), name='trustedcompany'), 
     path('trustedcompany/<int:pk>/', TrustedCompanyUpdateDelete.as_view(), name='trustedcompany'),

     path('projectdetail/', ProjectDetailsView.as_view(), name='projectdetail'), 
     path('projectdetail/<int:pk>/', ProjectDetailsUpdateDelete.as_view(), name='projectdetail'),

     path('empapprovdetail/', EmployeeApproveDetailView.as_view(), name='empapprovdetail'), 
     path('empapprovdetail/<int:pk>/', EmployeeAprroveUpdateDelete.as_view(), name='empapprovdetail'),








   
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


