from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, default="null")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    terms_and_conditions = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    
from django.utils import timezone
from datetime import timedelta
class EmployeeDetails(models.Model):
    CHOICES = (
  ('25%', '25%'),
  ('50%', '50%'),
  ('75%', '75%'),
  ('100%', '100%')
)
    name = models.CharField(max_length=2332)  
    task = models.CharField(max_length=2332)
    task_date = models.CharField(max_length=255,default='null')
    # from_date = models.DateField(null=True, blank=True)
    # To_date = models.DateField(null=True, blank=True)
    report_of_work = models.CharField(max_length=2332)
    completion_status = models.CharField(choices=CHOICES, max_length=128,default='25%')
    documnet = models.FileField(upload_to='', blank=False, null=True)
    comment = models.CharField(max_length=2332)
    document_base64 = models.TextField(blank=True, null=True)
    organization = models.CharField(max_length=255, blank=False, null=True, default=None)

    # def save(self, *args, **kwargs):
    #     # Call the original save method
    #     super().save(*args, **kwargs)

    #     # Calculate the cutoff date (today - 60 days)
    #     cutoff_date = timezone.now() - timedelta(days=60)
        
    #     # Delete records older than the cutoff date
    #     EmployeeDetails.objects.filter(task_date__lt=cutoff_date).delete()


class LoginProfile(models.Model):
    image = models.ImageField(upload_to='user_images/',blank=False, null=False)
    userid = models.CharField(max_length=20, unique=True,blank=False, null=False)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    blood_group = models.CharField(max_length=100,blank=False, null=False)
    dob = models.CharField(max_length=100,blank=False, null=False)
    image_base64 = models.TextField(blank=True, null=True)
    organization = models.CharField(max_length=255, blank=False, null=True, default=None)
    role = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True, blank=True, null=True)  # Changed to CharField
    reporting_to = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)  # Changed to CharField
    insta_link = models.CharField(max_length=200, blank=True, null=True)  # Changed to CharField
    linkedin_link = models.CharField(max_length=200, blank=True, null=True)  # Changed to CharField
    twitter_link = models.CharField(max_length=200, blank=True, null=True)  # Changed to CharField
    working_since = models.CharField(max_length=255, blank=True, null=True)
    earned_leave = models.CharField(max_length=255, blank=True, null=True)
    sick_leave = models.CharField(max_length=255, blank=True, null=True)
    casual_leave = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True) # add new filed phonenumber



    def __str__(self):
        return self.name


class EmployeeLogin(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # You can adjust the max_length as needed
    name = models.CharField(max_length=2322 , null=False,blank=False,default="") 
    tl = models.BooleanField(default=False)
    testing = models.BooleanField(default=False)
    testing_tl = models.BooleanField(default=False)
    backend = models.BooleanField(default=False)
    backend_tl = models.BooleanField(default=False)
    organization = models.CharField(max_length=255, blank=False, null=True, default=None)







    def __str__(self):
        return self.username


class EmployeeLogin2(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    date = models.CharField(max_length=255,null=True,blank=True)
    login_time = models.CharField(max_length=255,null=True,blank=True)
    longitude1 = models.CharField(max_length=255,null=True,blank=True)
    lattiude1 = models.CharField(max_length=255,null=True,blank=True)
    logout_time = models.CharField(max_length=255,null=True,blank=True)
    longitude2 = models.CharField(max_length=255,null=True,blank=True)
    lattiude2 = models.CharField(max_length=255,null=True,blank=True)
    total_time = models.CharField(max_length=255,null=True,blank=True)
    organization = models.CharField(max_length=255, blank=False, null=True, default=None)
    lunch_break_checkin = models.CharField(max_length=255, null=True, blank=True)
    lunch_break_checkout = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    approved = models.BooleanField(default=False)
    absent = models.BooleanField(default=False)
################################### logout and lunchbreak is missing and if all field fillup except reason ##########################
    def save(self, *args, **kwargs):
        # Check if either lunch break or logout is missing
        if not self.lunch_break_checkout or not self.logout_time:
            self.absent = True
        else:
            self.absent = False

        # Check if external approval is provided (via EmployeeApprovDetails)
        try:
            employee_approv_details = EmployeeApprovDetails.objects.get(emp_id=self.id)
            if employee_approv_details.emp_approve:
                self.approved = True
            else:
                self.approved = False
        except EmployeeApprovDetails.DoesNotExist:
            # If no external approval details found, use internal approval logic
            field_check = [
                self.name, self.date, self.login_time, self.longitude1,
                self.lattiude1, self.logout_time, self.longitude2, self.lattiude2,
                self.total_time, self.organization, self.lunch_break_checkin, self.lunch_break_checkout
            ]
            if all(field_check):
                self.approved = True
            else:
                self.approved = False

        super(EmployeeLogin2, self).save(*args, **kwargs)           





from datetime import datetime
class AssignTask(models.Model):
    assignee_name = models.CharField(max_length=255,null=True,blank=True)
    project_name = models.CharField(max_length=255,null=True,blank=True)
    tl_name = models.CharField(max_length=255,null=True,blank=True)
    task_name = models.CharField(max_length=255,null=True,blank=False)
    due_date  = models.DateTimeField(default=None)
    overdue_duedate = models.BooleanField(default=False)
    task_done = models.BooleanField(default=False)
    push_code = models.BooleanField(default=False)
    dev_review = models.BooleanField(default=False)
    add_photo = models.ImageField(upload_to='task_photos/', null=True, blank=True)
    addphoto_base64 = models.TextField(blank=True, null=True)
    task_description = models.TextField(null=True, blank=True)
    testing = models.BooleanField(default=False)
    testing_bug = models.BooleanField(default=False)
    deployment = models.BooleanField(default=False)
    re_deployment = models.BooleanField(default=False)
    re_testing = models.BooleanField(default=False)
    organization = models.CharField(max_length=255, blank=False, null=True, default=None)
    postdate = models.CharField(max_length=255, null=True, blank=True) # New field for postdate
    tester = models.CharField(max_length=255, null=True, blank=True)  # New field for tester
    dummyone = models.CharField(max_length=255, null=True, blank=True)  



    def save(self, *args, **kwargs):
        if self.due_date:
            # Adjust the specific time (e.g., 17:00:00 for 5:00 PM)
            due_datetime = datetime.combine(self.due_date, datetime.min.time()) + timedelta(hours=17)

            # Check if the current date and time are greater than the adjusted due date and time
            if datetime.now() > due_datetime:
                self.overdue_duedate = True
            else:
                self.overdue_duedate = False

        super(AssignTask, self).save(*args, **kwargs)


    def __str__(self):
        return self.task_name
    
class AdminAuth(models.Model):
    username=models.CharField(max_length=2322,null=False)
    password =models.CharField(max_length=2322,null=False)
    name=models.CharField(max_length=2322,null=True)
    organization = models.CharField(max_length=255, blank=False, null=True, default=None)




from django.db import models

class EmployeeJoining(models.Model):
    employeeName = models.CharField(max_length=255)
    employeeId = models.CharField(max_length=50)
    totalwork = models.CharField(max_length=50)
    leaves = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    dateOfJoining = models.CharField(max_length=20)
    month = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    basicDA = models.CharField(max_length=50)
    providentFund = models.CharField(max_length=50)
    hra = models.CharField(max_length=50)
    esi = models.CharField(max_length=50)
    conveyance = models.CharField(max_length=50)
    loan = models.CharField(max_length=50)
    professionTax = models.CharField(max_length=50)
    lop = models.CharField(max_length=50)
    totalAddition = models.CharField(max_length=50)
    totalDeduction = models.CharField(max_length=50)
    netSalary = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=255, default=False)
    ifsc = models.CharField(max_length=255,default=False)
    acc_num = models.CharField(max_length=255,default=False)
    branch_name = models.CharField(max_length=255,default=False)
    extrafil_1 = models.CharField(max_length=255,default=False)
    extrafil_2 = models.CharField(max_length=255,default=False)
    organization = models.CharField(max_length=255, blank=False, null=True, default=None)




    def __str__(self):
        return self.employeeName



class AddUser(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    tl = models.BooleanField(default=False)
    testing = models.BooleanField(default=False)
    testing_tl = models.BooleanField(default=False)
    backend = models.BooleanField(default=False)
    backend_tl = models.BooleanField(default=False)
    

class ApplyLeaves(models.Model):
    # SICK_LEAVE = 'sick_leave'
    # CASUAL_LEAVE = 'casual_leave'

    # LEAVE_TYPE_CHOICES = [
    #     (SICK_LEAVE, 'Sick Leave'),
    #     (CASUAL_LEAVE, 'Casual Leave'),
    # ]
    name = models.ForeignKey(LoginProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    tlname = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    reason = models.CharField(max_length=255)
    leave_type = models.CharField(max_length=50, null=True,blank=True) ## update this field as charfield
    posted_date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='leave_images/', null=True, blank=True)
    from_date = models.CharField(max_length=100)
    to_date = models.CharField(max_length=100)
    description = models.TextField()
    admin_approve = models.BooleanField(default=False)
    admin_cancel = models.BooleanField(default=False)
    tl_approve = models.BooleanField(default=False)
    tl_cancel = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.admin_approve and self.tl_approve:
            try:
                # Get the associated LoginProfile
                login_profile = LoginProfile.objects.get(name=self.name)

                # Decrease the count based on leave_type
                if self.leave_type == 'sick_leave':
                    if int(login_profile.sick_leave) > 0:
                        login_profile.sick_leave = str(int(login_profile.sick_leave) - 1)
                elif self.leave_type == 'casual_leave':
                    if int(login_profile.casual_leave) > 0:
                        login_profile.casual_leave = str(int(login_profile.casual_leave) - 1)
                
                # Save the updated LoginProfile
                login_profile.save()
            except LoginProfile.DoesNotExist:
                # Handle the case where the associated LoginProfile doesn't exist
                pass
        
        # Call the original save method to save the ApplyLeaves instance
        super().save(*args, **kwargs)


    def __str__(self):
        return self.subject

class Media(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    department = models.CharField(max_length=100)
    organization = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='media_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='media_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='media_images/', null=True, blank=True)
    video = models.FileField(upload_to='media_videos/', null=True, blank=True)
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Feed(models.Model):
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    image = models.ImageField(upload_to='feed_images/',null=True,blank=True)
    date = models.CharField(max_length=100)
    desc = models.TextField()

   




class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class WantedApi(models.Model):
    images = models.ManyToManyField(Image)
    description = models.TextField()
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    event_type=models.CharField(max_length=100,default=None)



class Image2(models.Model):
    image = models.ImageField(upload_to='images/')

class MultiplImages(models.Model):
    images = models.ManyToManyField(Image2)
    video = models.FileField(upload_to='media_videos/', null=True, blank=True)
    description = models.TextField()
    organization = models.CharField(max_length=255)
    date = models.CharField(max_length=100)


class Holiday(models.Model):
    date = models.CharField(max_length=255)
    holidayname = models.CharField(max_length=255)
    week = models.CharField(max_length=255)
    image = models.ImageField(upload_to='holiday_images/')
    desc = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    
    
    
class Image3(models.Model):
    image = models.ImageField(upload_to='images/')   

class AdminApi(models.Model):
    name = models.CharField(max_length=100, unique=True)
    organization = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='logos/')
    company_type = models.CharField(max_length=100)
    company_since = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    company_address = models.TextField()
    social_media_links = models.JSONField(default=dict)  # Store social media links as a JSON field
    about = models.TextField()
    images = models.ManyToManyField(Image)
    tagline = models.CharField(max_length=255)
    no_of_employees = models.PositiveIntegerField(default=0)
    domain = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    email =models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def set_social_media_link(self, platform, link):
        self.social_media_links[platform] = link

    def get_social_media_link(self, platform):
        return self.social_media_links.get(platform, None)

    def __str__(self):
        return self.name
    
class TrustedCompany(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='company_logo/')
    websiteurl = models.CharField(max_length=100,null=True,blank=True)    

class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

class ProjectDetails(models.Model):
    projectname = models.CharField(max_length=255,null=True,blank=True)
    logo = models.ImageField(upload_to='project_logo/')
    employeename = models.CharField(max_length= 255,null=True,blank=True)    

class  EmployeeApprovDetails(models.Model):
    name= models.CharField(max_length=255,null=True,blank=True)
    emp_id=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    emp_approve = models.BooleanField(default=False) 

############# approve check box as per condition #########
    def save(self, *args, **kwargs):
        super(EmployeeApprovDetails, self).save(*args, **kwargs)

        # Update the 'approved' field in EmployeeLogin2 only if emp_approve is explicitly set to True
        if self.emp_approve:
            try:
                emp = EmployeeLogin2.objects.get(pk=self.emp_id)
                emp.approved = True
                emp.save()
            except EmployeeLogin2.DoesNotExist:
                pass  # Handle the case where the associated EmployeeLogin2 instance does not exist 
