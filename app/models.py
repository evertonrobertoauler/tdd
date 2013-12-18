from django.core.urlresolvers import reverse
from django.db import models
import random
import string
import datetime


class Articles(models.Model):
    title = models.CharField(max_length=140, default=random.choice(string.ascii_lowercase))
    body = models.TextField(default=random.choice(string.ascii_lowercase))
    slug = models.SlugField(unique=True, max_length=255, default=random.choice(string.ascii_lowercase))
    created = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app.views.post', args=[self.slug])