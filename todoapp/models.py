from django.db import models
from login.models import User
import datetime

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.todo+", "+str(self.date)+", Done: "+str(self.done)


