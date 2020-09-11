import uuid
from django.db import models
from drf_firebase_auth.models import FirebaseUser


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mac = models.CharField(max_length=17, unique=True)
    description = models.CharField(max_length=50)
    account_id = models.ForeignKey(FirebaseUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description     
