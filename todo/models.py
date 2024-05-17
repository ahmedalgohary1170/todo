from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True , null=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title