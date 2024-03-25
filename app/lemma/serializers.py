from rest_framework import serializers
from .models import Lemma


class LemmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lemma
        fields = ('word')
