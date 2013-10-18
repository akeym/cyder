from rest_framework import serializers

from cyder.api.v1.endpoints.dhcp import api
from cyder.cydhcp.interface.dynamic_intr.models import (DynamicInterface,
                                                        DynamicIntrKeyValue)


class DynamicIntrKeyValueSerializer(serializers.ModelSerializer):
    id = serializers.Field(source='id')
    dynamic_interface = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='api-dhcp-dynamicinterface-detail')

    class Meta:
        model = DynamicIntrKeyValue


class DynamicIntrKeyValueViewSet(api.CommonDHCPViewSet):
    model = DynamicIntrKeyValue
    serializer_class = DynamicIntrKeyValueSerializer


class DynamicIntrNestedKeyValueSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(
        view_name='api-dhcp-dynamicinterface_keyvalues-detail')

    class Meta:
        model = DynamicIntrKeyValue
        fields = api.NestedKeyValueFields


class DynamicInterfaceSerializer(serializers.ModelSerializer):
    dynamicintrkeyvalue_set = DynamicIntrNestedKeyValueSerializer(many=True)
    system = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='api-core-system-detail')
    domain = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='api-dns-domain-detail')
    range = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='api-dhcp-range-detail')
    ctnr = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='api-core-ctnr-detail')
    workgroup = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='api-dhcp-workgroup-detail')

    class Meta(api.CommonDHCPMeta):
        model = DynamicInterface
        depth = 1


class DynamicInterfaceViewSet(api.CommonDHCPViewSet):
    model = DynamicInterface
    serializer_class = DynamicInterfaceSerializer
    keyvaluemodel = DynamicIntrKeyValue