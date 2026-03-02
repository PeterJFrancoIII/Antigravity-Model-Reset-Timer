from django.db import models

class AntigravityAccount(models.Model):
    # Unique account identifier
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Absolute future UTC timestamps for when timers hit zero
    gemini_flash_reset = models.DateTimeField(null=True, blank=True)
    gemini_pro_reset = models.DateTimeField(null=True, blank=True)
    opus_sonnet_reset = models.DateTimeField(null=True, blank=True)

    # Percentage remaining for each model
    gemini_flash_percent = models.IntegerField(default=100)
    gemini_pro_percent = models.IntegerField(default=100)
    opus_sonnet_percent = models.IntegerField(default=100)

    def __str__(self):
        return self.name
