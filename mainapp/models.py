from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=120)
    business = models.CharField(max_length=160)
    phone = models.CharField(max_length=40)
    service = models.CharField(max_length=60)
    source = models.CharField(max_length=40, default='lead_form', blank=True)
    user_agent = models.CharField(max_length=300, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.business} ({self.created_at:%Y-%m-%d})'
