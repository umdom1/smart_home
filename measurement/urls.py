from django.urls import path
from measurement.views import SensorAPIList, SensorAPIUpdate, MeasurementAPICreate, SensorAPIRetrieve

urlpatterns = [
    path('sensorslistall/', SensorAPIList.as_view()),
    path('sensorsupdate/<int:pk>/', SensorAPIUpdate.as_view()),
    path('tempadd/', MeasurementAPICreate.as_view()),
    path('sensorslist/<int:pk>/', SensorAPIRetrieve.as_view()),
]
