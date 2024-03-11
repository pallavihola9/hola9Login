from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(User)
class Users(UserAdmin):
    list_display = ('email', 'full_name', 'is_active', 'is_admin', 'is_staff', 'terms_and_conditions')
    search_fields = ('email', 'full_name')
    list_filter = ('is_active', 'is_admin', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff')}),
        ('Terms and Conditions', {'fields': ('terms_and_conditions',)}),  # Add this line

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'terms_and_conditions'),
        }),
    )
    ordering = ('email',)
    
    # Customize filter_horizontal based on your model's attributes
    filter_horizontal = ()

    # Optionally, you can add other related fields here if needed
    # filter_horizontal = ('some_related_field',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            # Creating a new user, so don't display 'user_permissions' and 'groups' fields
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

admin.site.register(EmployeeDetails)
admin.site.register(LoginProfile)
admin.site.register(EmployeeLogin)
admin.site.register(EmployeeLogin2)
admin.site.register(AssignTask)
admin.site.register(AdminAuth)
admin.site.register(EmployeeJoining)

admin.site.register(AddUser)
admin.site.register(ApplyLeaves)
admin.site.register(Media)
admin.site.register(Feed)
admin.site.register(Image)
admin.site.register(WantedApi)
admin.site.register(Image2)
admin.site.register(MultiplImages)
admin.site.register(Holiday)
admin.site.register(Image3)
admin.site.register(AdminApi)   
admin.site.register(TrustedCompany)
admin.site.register(ProjectDetails)
admin.site.register(EmployeeApprovDetails) 










