from factory.django import DjangoModelFactory

from . import models


class SlotFactory(DjangoModelFactory):
    class Meta:
        model = models.Slot
