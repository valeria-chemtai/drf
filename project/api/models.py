from django.db import models


class Bucketlist(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    interesting = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    bucketlist_pk = models.ForeignKey(
        Bucketlist, related_name='items', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.name
