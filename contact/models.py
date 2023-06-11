from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Us'

    name = models.CharField(max_length=254)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return f"Message {self.body} from {self.name}"