from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema

from .models import Slot
from .serializers import SlotSerializer


class SlotSchema(AutoSchema):
    def get_serializer(self, path, method):
        return SlotSerializer()


@api_view(["GET"])
@schema(SlotSchema())
def slot_list(request, item_id):
    """
    Return a list of all available slots.
    """
    slots = Slot.objects.filter(item_id=item_id).order_by("date")
    serializer = SlotSerializer(slots, many=True)
    return Response(serializer.data)
