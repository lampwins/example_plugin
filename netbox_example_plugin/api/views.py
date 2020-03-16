from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return Response({'message': 'Hello World!'})
