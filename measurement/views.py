from rest_framework import generics

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


class SensorAPIList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementAPICreate(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorAPIRetrieve(generics.RetrieveDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
