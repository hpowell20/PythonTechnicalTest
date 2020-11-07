from rest_framework import serializers

from .models import Bond
from .utils import get_lei_legal_name


class BondWriteSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer used to save the record
    """

    def validate(self, data):
        try:
            data['legal_name'] = get_lei_legal_name(data['lei'])
            return data
        except Exception as e:
            error = {'lei': [e]}
            raise serializers.ValidationError(error)

    class Meta:
        model = Bond
        fields = ('lei', 'isin', 'size', 'currency', 'maturity')


class BondReadSerializer(serializers.ModelSerializer):
    """
    Serializer used to read the record
    """
    class Meta:
        model = Bond
        fields = ('lei', 'legal_name', 'isin', 'size', 'currency', 'maturity')
