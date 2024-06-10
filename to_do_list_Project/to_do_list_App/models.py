from django.db import models
from django.contrib.auth.models import AbstractUser


class custom_user(AbstractUser):
    USERTYPE=[
        ('user','User'),
        ('admin','Admin'),
    ]
    
    user_type=models.CharField(choices=USERTYPE,max_length=100, null=True)
    city=models.CharField(max_length=100, null=True)
    profile_picture=models.ImageField(upload_to='media/profile_picture',null=True)

    class Meta:
        ordering=['username']
        verbose_name= 'Custom User'
        db_table='my_to_do_list_table'


class category_model(models.Model):
    catuser=models.ForeignKey(custom_user,on_delete=models.CASCADE,null=True)
    category_name=models.CharField(max_length=100, null=True)
    created_at=models.DateField(auto_now_add=True, null=True)
    updated_at=models.DateField(auto_now=True, null=True)


class task_model(models.Model):
    taskuser=models.ForeignKey(custom_user,on_delete=models.CASCADE,null=True)
    task_category=models.ForeignKey(category_model,on_delete=models.CASCADE,null=True)
    task_name=models.CharField(max_length=100, null=True)
    task_description=models.TextField(null=True)
    task_status=models.CharField(default='on_going',max_length=100, null=True)

    PRIORITY=[
        ('high','High'),
        ('medium','Medium'),       
        ('low','Low'),       
    ]
    task_priority=models.CharField(choices=PRIORITY,default='on_going',max_length=100, null=True)
    due_date=models.DateField(null=True)
    completed_date=models.DateField(null=True)
    created_at=models.DateField(auto_now_add=True, null=True)
    updated_at=models.DateField(auto_now=True, null=True)
