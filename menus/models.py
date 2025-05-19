from django.db import models
from django.utils.text import slugify

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = f'{slugify(self.name)}/'
        super().save(*args, **kwargs)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    named_url = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.named_url:  # Only generate if URL is empty
            parent_url = self.menu.url if self.parent is None else self.parent.url
            self.url = f'{parent_url}{slugify(self.name)}/'
