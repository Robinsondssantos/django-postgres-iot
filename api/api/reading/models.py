from django.db import models

class Reading(models.Model):
    device_id = models.CharField(max_length=36, db_index=True)
    temperature = models.FloatField()
    rec_at = models.CharField(max_length=19)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_id               
