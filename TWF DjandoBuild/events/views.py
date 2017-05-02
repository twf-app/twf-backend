from datetime import timedelta

from django.utils import timezone
from geoposition import Geoposition
from rest_framework import viewsets, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Journey, CheckIn
from events.serializers import CheckInSerializer, JourneySerializer
from places.models import Zone, Location


class MemberCheckinViewSet(APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        """
        GET Nearby_users, if NOT request.user
        :param request: GET
        :param args: Member, Geolocation, Time, Radius
        :return: Users checked-into radius of user within last 2 hours.
        """
        time = timezone.localtime(timezone.now())
        past_timestamp = time - timedelta(hours=2)
        # lat = request.GET['lat']
        # lng = request.GET['lng']
        # radius_meters = request.GET['radius']
        # pos = Geoposition(lat, lng)

        # Return USERS by timestamp within a range. (queryset)
        nearby_users = CheckIn.objects.filter(time__range=(past_timestamp, time)).exclude(member__pk=request.user.pk)
        serializer = CheckInSerializer(nearby_users, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def post(self, request, *args, **kwargs):
        """
        POST USER LOCATION AS CHECK-IN
        :param request: POST
        :param args: Member, Geolocation, Time, Radius
        """
        member = request.user
        time = timezone.now()
        lat = request.POST['lat']
        lng = request.POST['lng']
        radius_meters = request.POST['radius']
        pos = Geoposition(lat, lng)

        location = Location(position=pos, created_time=time)
        location.save()

        zone = Zone(location=location, radius_meters=radius_meters)
        zone.save()

        check_in = CheckIn(member=member, time=time, zone=zone, location=location)
        check_in.save()

        serializer = CheckInSerializer(check_in, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CheckinViewSet(viewsets.ModelViewSet):
    model = CheckIn
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


class JourneyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
