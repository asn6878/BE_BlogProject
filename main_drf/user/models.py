from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, email, username, password=None):
        
        if not email :
            raise ValueError('must have user email')
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )        
        user.set_password(password)
        user.save(using=self._db) 
        return user
    def create_superuser(self, email, username,password ):        
       
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    # 사용자 관련된 필드 및 기본 권한 값
    username = models.CharField(max_length=255, unique=True, verbose_name='username')
    email = models.EmailField(max_length=255, unique=True, verbose_name='email')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True)

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)     

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return "<id : %d / username : %s>" % (self.id, self.username)
    
