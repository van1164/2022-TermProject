from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Account(models.Model):
    user_id = models.CharField(max_length=32, unique=True,primary_key=True,verbose_name='ID')
    password = models.CharField(max_length=20, verbose_name='PASSWORD')
    created_date = models.DateTimeField(
            default=timezone.now,verbose_name="계정 생성일")
    email = models.EmailField(max_length=128, unique=True, verbose_name='이메일')
    name = models.CharField(max_length=32,verbose_name="이름")
    interior = models.TextField(default='')#USER가 작업한 인테리어
    job = models.CharField(max_length=32,default='',verbose_name="직종") # 목수, 도배, 장판 등등
    star_address = models.TextField(default='')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Account'
        verbose_name='유저'
        verbose_name_plural='유저'

#모든 인테리어
class interior(models.Model):
    interior_name = models.CharField(max_length=30,unique=True,verbose_name='인테리어 제목')
    id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField(
        default=timezone.now,verbose_name="공사 시작일")
    end_date = models.DateTimeField(
        default=timezone.now,verbose_name="공사 종료일")
    address = models.CharField(max_length=30,unique=True,verbose_name='인테리어 제목')
    job = models.CharField(max_length=32,default='',verbose_name="직종") # 목수, 도배, 장판 등등
    class Meta:
        db_table = 'interior'
        verbose_name='interior'
        verbose_name_plural='interior'
        
    def __str__(self):
        return self.interior_name