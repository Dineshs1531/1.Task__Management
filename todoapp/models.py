from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Ourtask(models.Model):
    priority_choice = [
        ("Low",'Low'),
        ("Medium","Medium"),
        ("High","High"),
    ]
    user_id=models.ForeignKey(User,null=True,default=None,on_delete = models.SET_DEFAULT)
    title = models.CharField(max_length=191,null=False, blank=False,unique=True)
    description = models.TextField(null=False, blank=False)
    due_date = models.DateField(null=False, blank=False)
    priority = models.CharField(choices=priority_choice,null=True,blank=False,max_length=50)
    created_at = models.DateField(null=False, blank=False)
    updated_at = models.DateField(null=False, blank=False)
    Time = models.TimeField(null=False, blank=False)
    completed_status=models.BooleanField(default=False)

    def __str__(self):
        return self.title