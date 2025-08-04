from django.db import models

from account.models import CustomUser
from common.models import BaseModel


class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='project_own', null=True)
    members = models.ManyToManyField(CustomUser, related_name='project_members', blank=True)

    class Meta:
        db_table = 'projects'
        ordering = ('-created_at',)
        # unique_together = ('name','description')
