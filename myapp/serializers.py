from rest_framework import serializers
from . import models

class GejalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gejala
        fields = '__all__'

class PenyakitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Penyakit
        fields = '__all__'

class BasisPengetahuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasisPengetahuan
        fields = '__all__'

class DsRuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.DsRules
        fields = '__all__'

class RiwayatSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Riwayat
        fields = '__all__'