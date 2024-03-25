import json

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import Lemma
from .serializers import LemmaSerializer


class LemmaAPIView(generics.ListAPIView):

    queryset = Lemma.objects.all()
    serializer_class = LemmaSerializer

class MakeLemma(APIView):
    def get_lemma(self, str):
        return "NEW" + str
    def post(self, request):
        words = request.data['words']
        my_dict = {}

        for element in words:
            my_dict[element] = self.get_lemma(element)

        my_json = json.dumps(my_dict)

        return Response (my_json, status=HTTP_200_OK)
