from rest_framework import serializers

from . import models


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Slot
        fields = ["id", "date", "count", "item_id"]
