from django.db import models
from django import forms
from django.utils.text import slugify
import uuid


# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=False, null=False)
    image_url = models.URLField(blank=False)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    is_private = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_email = models.EmailField(max_length=50, blank=False)
    customer_name = models.CharField(max_length=64, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.customer_name