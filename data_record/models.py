from django.db import models
import datetime
from django.utils import timezone
#coding=utf-8
#定义一个数据库来储存所有的用户的用户名和密码
class Users(models.Model):
    user_name=models.CharField(max_length=30)
    user_password=models.CharField(max_length=40)
    use_email=models.EmailField()
# Create your models here.
#定义项目的列表，包括以下内容（项目名称，项目负责人，项目立项时间）
class Project(models.Model):
    project_name=models.CharField(max_length=20)
    person=models.CharField(max_length=20,blank=True)
    release_date=models.DateTimeField("date released",blank=True)
    def __str__(self):
        return self.project_name

#定义分析的路径历史，历史包括几个内容（文件夹名称，项目名称，分析日期，分析人）
class History(models.Model):
    #定义分析的文件夹名称
    folder_name=models.CharField(max_length=300)
    #定义分析的路径
    path_n=models.CharField(max_length=500)
    #定义分析的项目
    #project_name=models.CharField(max_length=20,default="000000")
    project_name=models.ForeignKey(Project,on_delete=models.CASCADE)
    #定义分析的时间
    pub_date=models.DateTimeField("date analyzed")
    #定义分析的人
    person_analysis=models.CharField(max_length=300) 
    def __str__(self):
        return self.folder_name
    def was_analyzed_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

        
