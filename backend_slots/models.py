from django.db import models


class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_id = models.CharField(max_length=40)

    class Meta:
        unique_together = (("item_id", "date"),)

    def __str__(self):
        return self.date
