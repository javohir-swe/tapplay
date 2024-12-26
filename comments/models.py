from django.db import models


class Like(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        unique_together = ('user', 'comment')


class Comment(models.Model):
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    audio_id = models.ForeignKey("audio.Audio", related_name="comments", blank=True, on_delete=models.CASCADE)  # Keyinchalik bu comment oddiy author bo'lmagan userlar uchun fikr bildirish uchun hizmat qilishi mumkin.
    likes = models.ManyToManyField("accounts.User", through=Like, related_name="liked_comments", blank=True)  # Like bosgan userlarning IDlarini saqlaydi va bitta useer bir marotaba like bosa oladi.

    objects = models.Manager()

    def __str__(self):
        return self.text[:20]
