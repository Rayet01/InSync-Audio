from django.db import models

class GuestMix(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_path = models.FileField(upload_to='guest_mixes/')
    description = models.TextField()
    upload_date = models.DateField()
    image = models.ImageField(upload_to='guest_mix_images/', null=True, blank=True)

    def __str__(self):
        return self.title
