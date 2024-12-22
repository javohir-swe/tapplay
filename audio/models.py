from django.db import models
from django.utils.translation import gettext_lazy as _


class Audio(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", _("Draft")
        PUBLISHED = "PUBLISHED", _("Published")
        FREEZE = "FREEZE", _("Freeze")

    status = models.CharField(choices=Status, default=Status.DRAFT)
    title = models.CharField(max_length=100)
    author = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField(upload_to="audio_media/thumbnails/")
    audio = models.FileField(upload_to="audio_media/audios/")
    total_time = models.CharField(max_length=20)
    # donate_ids = models.ManyToManyField()
    # comment_ids = models.ManyToManyField() # Alohida APIdan olinadi Audio IDsini bergan holatda

    def __str__(self):
        return self.title[:20]
