from django.db import models

class Reading(models.Model):
    device_id = models.CharField(max_length=50, blank=False, null=False, 
        db_index=True, default=0)
    temperature = models.FloatField(blank=True, null=True)
    rec_at = models.CharField(max_length=19, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_id        
