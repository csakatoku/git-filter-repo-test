from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView

from .serializers import VersionSerializer


class VersionSchema(AutoSchema):
    def get_operation_id(self, path, method):
        return "getVersion"

    def get_serializer(self, path, method):
        return VersionSerializer()


class VersionAPIView(APIView):
    schema = VersionSchema()

    def get(self, request):
        serializer = VersionSerializer({"version": "1.0.0"})
        return Response(serializer.data)
