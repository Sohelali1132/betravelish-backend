from rest_framework.viewsets import ModelViewSet
from .models import Trek
from .serializers import TrekSerializer

class TrekViewSet(ModelViewSet):
    queryset = Trek.objects.all()
    serializer_class = TrekSerializer
