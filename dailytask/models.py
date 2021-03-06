# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    任务类
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 创建任务人
    content = models.CharField(max_length=255) # 任务内容
    parent = models.IntegerField(default=0) # 父任务id，默认为0
    create_date = models.DateTimeField(auto_now_add=True) # 任务创建时间
    done_date = models.DateTimeField(null=True) # 任务完成时间
    have_completed = models.BooleanField(default=False) # 是否已经完成
    
    def __str__(self):
        return self.user.username + "|" + self.content
