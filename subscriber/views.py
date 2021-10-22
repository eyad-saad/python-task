import base64
from datetime import datetime
import pickle

from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import make_aware
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from subscriber.models import DeviceEntry


class HandleMessage(APIView):
    def post(self, request):
        envelope = request.data
        payload = base64.b64decode(envelope['message']['data'])
        data = pickle.loads(payload)['data']

        device_entry = DeviceEntry()
        device_entry.device_id = data['deviceId']
        device_entry.temperature = data['temperature']
        device_entry.longitude = data['location']['longitude']
        device_entry.latitude = data['location']['latitude']
        device_entry.time = make_aware(datetime.fromtimestamp(data['time']))
        device_entry.save()

        return Response({}, status=HTTP_200_OK)


class MaxTemperature(APIView):
    def get(self, request):
        device_id = request.GET.get("device-id")
        for device_entry in DeviceEntry.objects.raw('SELECT *, MAX(temperature) as max_temperature FROM device_entry GROUP BY `device_id`;'):
            if str(device_id) == str(device_entry.device_id):
                return Response({'max_temperature': device_entry.temperature})
        return Response({'message': 'could not find device'}, status=HTTP_400_BAD_REQUEST)


class DataPointCount(APIView):
    def get(self, request):
        device_id = request.GET.get("device-id")
        count = DeviceEntry.objects.filter(device_id=device_id).count()
        return Response({'count': count})


class MaxTemperaturePerDay(APIView):
    def get(self, request):
        date = request.GET.get("date")
        device_id = request.GET.get("device-id")
        for device_entry in DeviceEntry.objects.raw("""SELECT *, MAX(temperature) as max_temperature FROM device_entry WHERE time BETWEEN 
        '{} 00:00:00' AND '{} 23:59:59'  GROUP BY `device_id`;""".format(date, date)):
            if device_id == str(device_entry.device_id):
                return Response({'max_temperature': device_entry.temperature})
        return Response({'message': 'could not find device'}, status=HTTP_400_BAD_REQUEST)
