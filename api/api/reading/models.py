from django.db import models

class Reading(models.Model):
    mac = models.CharField(max_length=17, blank=False, null=False, db_index=True)
    at = models.FloatField(blank=True, null=True)
    rec_at = models.CharField(max_length=19, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    
