from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # custom user model with role based acess 
    ROLE_CHOICES=(
        ('farmer','Farmer'),
        ('porter','Porter'),
        ('admin','Admin')
    )
    role= models.CharField(max_length=10,choices=ROLE_CHOICES,default='farmer')
    phone_number=models.CharField(max_length=15,unique=True)
    def __str__(self):
        return f"{self.username,{self.role}}"
    
class BaseModel(models.Model):
    # abstract class base model with common timestamps 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class FarmerProfile(BaseModel):
    # complete farmer profile all in for a cooperative need 
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')
    profile_image=models.ImageField(upload_to='farmer/profiles/',null=True,blank=True)
    national_id=models.CharField(max_length=15,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(max_length=10)
    gender=models.CharField(max_length=10, choices=[('MALE','Male'),('FEMALE','Female')])

    # contact info 
    phone_number=models.CharField(max_length=15,unique=True)
    alternative_phone=models.CharField(max_length=15,blank=True,null=True)
    email_address=models.EmailField(blank=True,null=True)

    # farmer info 
    farm_name=models.CharField(max_length=200,blank=True,null=True)
    farm_size_acres=models.DecimalField(max_length=200,blank=True,null=True,decimal_places=2)
    number_of_Cows=models.IntegerField(default=0)
    membership_number=models.CharField(max_length=50,blank=True,null=True)
    join_date=models.DateField(auto_now_add=True)
    mpesa_number=models.CharField(max_length=15,blank=True,null=True  , unique=True)

    # stats auto updated by system 
    total_milk_delivered=models.DecimalField(max_digits=12,decimal_places=2,default=0)
    total_earnings=models.DecimalField(max_digits=15,decimal_places=2,default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# ==================================================================
# porters profile 
# ===============================================

class PorterProfile(BaseModel):
    # profile 
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='porter_profile')
    profile_image=models.ImageField(upload_to='porter/profiles',null=True, blank=True)
    employee_id=models.CharField(max_length=20,unique=True)
    national_id=models.CharField(max_length=15,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    route_name=models.CharField(max_length=200)
    assigned_farmers=models.ManyToManyField(FarmerProfile,related_name='assigned_porters',blank=True,null=True)
    hire_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    total_collections=models.IntegerField(default=0)
    total_litres_collected=models.DecimalField(max_digits=12,decimal_places=2,default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}-{self.employee_id}"
    
class MilkCollection(BaseModel):
    # daily mlk collection records 
    SESSIONS=[
        ('MORNING','Morning'),
        ('EVENING','Evening')
    ]
    farmer=models.ForeignKey(FarmerProfile,on_delete=models.CASCADE,related_name='collections')
    porter=models.ForeignKey(PorterProfile,on_delete=models.CASCADE)
    litres=models.DecimalField(max_digits=10,decimal_places=2)
    session=models.CharField(max_length=10,choices=SESSIONS)
    collection_date=models.DateField(auto_now_add=True)
    price_per_litre=models.DecimalField(max_digits=8,decimal_places=2,default=50)
    total_amount=models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return f"{self.collection_date}: {self.farmer.first_name}-{self.litres}"

