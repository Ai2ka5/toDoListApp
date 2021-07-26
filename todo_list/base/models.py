from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name=_("Title"), max_length=200, null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    complete = models.BooleanField(verbose_name=_("Complete"), default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']